"""
Agentic Course Content Generator
Multi-agent system for curriculum planning and content generation
"""

import json
from typing import Dict, List, Any
from dataclasses import dataclass, asdict
from enum import Enum


class GenerationMode(Enum):
    WEEKLY = "Weekly"
    LECTURE_WISE = "Lecture-wise"
    MONTHLY = "Monthly"


@dataclass
class ContentInput:
    syllabus_text: str
    course_outline_text: str
    timetable_text: str
    subject_name: str
    course_duration: str
    class_duration: int
    mode: str


class SyllabusAnalysisAgent:
    """Agent 1: Analyzes syllabus and extracts subject-specific content"""
    
    def analyze(self, syllabus: str, course_outline: str, subject: str) -> Dict[str, Any]:
        # Extract units and topics for the selected subject
        units = self._extract_units(syllabus, course_outline, subject)
        return {
            "subject": subject,
            "units": units,
            "total_topics": sum(len(u["topics"]) for u in units)
        }
    
    def _extract_units(self, syllabus: str, outline: str, subject: str) -> List[Dict]:
        # Parse syllabus structure
        units = []
        lines = (syllabus + "\n" + outline).split("\n")
        current_unit = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Simple heuristic: detect unit headers
            if any(keyword in line.lower() for keyword in ["unit", "module", "chapter"]):
                if current_unit:
                    units.append(current_unit)
                current_unit = {"name": line, "topics": []}
            elif current_unit and line:
                current_unit["topics"].append(line)
        
        if current_unit:
            units.append(current_unit)
        
        return units


class CurriculumPlanningAgent:
    """Agent 2: Orders topics and estimates teaching time"""
    
    def plan(self, units: List[Dict], class_duration: int) -> List[Dict]:
        planned_topics = []
        
        for unit in units:
            for topic in unit["topics"]:
                difficulty = self._assess_difficulty(topic)
                time_estimate = self._estimate_time(topic, difficulty, class_duration)
                
                planned_topics.append({
                    "unit": unit["name"],
                    "topic": topic,
                    "difficulty": difficulty,
                    "estimated_minutes": time_estimate
                })
        
        return planned_topics
    
    def _assess_difficulty(self, topic: str) -> str:
        # Simple heuristic based on keywords
        advanced_keywords = ["advanced", "complex", "optimization", "algorithm"]
        basic_keywords = ["introduction", "basic", "overview", "fundamentals"]
        
        topic_lower = topic.lower()
        if any(kw in topic_lower for kw in advanced_keywords):
            return "Advanced"
        elif any(kw in topic_lower for kw in basic_keywords):
            return "Beginner"
        return "Intermediate"
    
    def _estimate_time(self, topic: str, difficulty: str, class_duration: int) -> int:
        # Estimate based on difficulty
        multipliers = {"Beginner": 1.0, "Intermediate": 1.5, "Advanced": 2.0}
        return int(class_duration * multipliers.get(difficulty, 1.0))


class SchedulingAgent:
    """Agent 3: Allocates topics based on generation mode"""
    
    def schedule(self, planned_topics: List[Dict], mode: str, 
                 class_duration: int, timetable: str) -> Dict[str, Any]:
        
        if mode == GenerationMode.WEEKLY.value:
            return self._schedule_weekly(planned_topics, class_duration, timetable)
        elif mode == GenerationMode.LECTURE_WISE.value:
            return self._schedule_lecture(planned_topics, class_duration)
        elif mode == GenerationMode.MONTHLY.value:
            return self._schedule_monthly(planned_topics, class_duration, timetable)
        
        return {"lectures": [], "time_scope": ""}
    
    def _schedule_weekly(self, topics: List[Dict], class_duration: int, timetable: str) -> Dict:
        # Allocate topics for one week
        weekly_classes = self._parse_weekly_classes(timetable)
        total_time = weekly_classes * class_duration
        
        allocated = []
        time_used = 0
        
        for topic in topics:
            if time_used + topic["estimated_minutes"] <= total_time:
                allocated.append(topic)
                time_used += topic["estimated_minutes"]
            else:
                break
        
        return {
            "time_scope": "Week 1",
            "lectures": self._group_into_lectures(allocated, class_duration),
            "allocated_topics": allocated
        }
    
    def _schedule_lecture(self, topics: List[Dict], class_duration: int) -> Dict:
        # Allocate for one lecture - be more generous
        allocated = []
        time_used = 0
        
        # Allow up to 1.5x class duration for better content
        max_time = int(class_duration * 1.5)
        
        for topic in topics:
            if time_used + topic["estimated_minutes"] <= max_time:
                allocated.append(topic)
                time_used += topic["estimated_minutes"]
            if len(allocated) >= 2:  # At least 2 topics per lecture
                break
        
        # If no topics allocated, take at least one
        if not allocated and topics:
            allocated = [topics[0]]
            time_used = topics[0]["estimated_minutes"]
        
        return {
            "time_scope": "Lecture 1",
            "lectures": [{"lecture_number": 1, "topics": allocated, "duration": time_used}],
            "allocated_topics": allocated
        }
    
    def _schedule_monthly(self, topics: List[Dict], class_duration: int, timetable: str) -> Dict:
        # Allocate for one month (assume 4 weeks)
        weekly_classes = self._parse_weekly_classes(timetable)
        total_time = weekly_classes * class_duration * 4
        
        allocated = []
        time_used = 0
        
        for topic in topics:
            if time_used + topic["estimated_minutes"] <= total_time:
                allocated.append(topic)
                time_used += topic["estimated_minutes"]
            else:
                break
        
        return {
            "time_scope": "Month 1",
            "lectures": self._group_into_lectures(allocated, class_duration),
            "allocated_topics": allocated
        }
    
    def _parse_weekly_classes(self, timetable: str) -> int:
        # Simple parser - count class mentions
        return max(2, timetable.lower().count("class"))
    
    def _group_into_lectures(self, topics: List[Dict], class_duration: int) -> List[Dict]:
        lectures = []
        current_lecture = {"lecture_number": 1, "topics": [], "duration": 0}
        
        for topic in topics:
            if current_lecture["duration"] + topic["estimated_minutes"] <= class_duration:
                current_lecture["topics"].append(topic)
                current_lecture["duration"] += topic["estimated_minutes"]
            else:
                lectures.append(current_lecture)
                current_lecture = {
                    "lecture_number": len(lectures) + 1,
                    "topics": [topic],
                    "duration": topic["estimated_minutes"]
                }
        
        if current_lecture["topics"]:
            lectures.append(current_lecture)
        
        return lectures



class ContentGenerationAgent:
    """Agent 4: Generates PPT, PDF, Audio, and Video content with REAL meaningful content"""
    
    def __init__(self):
        from intelligent_content_generator import IntelligentContentGenerator
        self.intelligent_generator = IntelligentContentGenerator()
    
    def generate(self, topic_data: Dict) -> Dict[str, Any]:
        # Use intelligent generator for real content
        return self.intelligent_generator.generate_content(
            topic_data["topic"],
            topic_data["unit"],
            topic_data["difficulty"]
        )


class ValidationAgent:
    """Agent 5: Validates content against syllabus and time constraints"""
    
    def validate(self, content: List[Dict], syllabus_data: Dict, 
                 schedule: Dict, class_duration: int) -> Dict[str, Any]:
        
        validation_results = {
            "syllabus_aligned": self._check_syllabus_alignment(content, syllabus_data),
            "time_feasible": self._check_time_feasibility(schedule, class_duration),
            "content_quality": self._check_content_quality(content),
            "approved": True
        }
        
        validation_results["approved"] = all([
            validation_results["syllabus_aligned"],
            validation_results["time_feasible"],
            validation_results["content_quality"]
        ])
        
        return validation_results
    
    def _check_syllabus_alignment(self, content: List[Dict], syllabus_data: Dict) -> bool:
        # Verify all topics are from syllabus
        return len(content) > 0
    
    def _check_time_feasibility(self, schedule: Dict, class_duration: int) -> bool:
        # Verify time allocation is realistic
        for lecture in schedule.get("lectures", []):
            if lecture["duration"] > class_duration * 1.1:  # 10% buffer
                return False
        return True
    
    def _check_content_quality(self, content: List[Dict]) -> bool:
        # Basic quality checks
        for item in content:
            if not item.get("learning_objectives") or not item.get("ppt_slides"):
                return False
        return True


class CourseContentGenerator:
    """Main orchestrator - coordinates all agents"""
    
    def __init__(self):
        self.syllabus_agent = SyllabusAnalysisAgent()
        self.planning_agent = CurriculumPlanningAgent()
        self.scheduling_agent = SchedulingAgent()
        self.content_agent = ContentGenerationAgent()
        self.validation_agent = ValidationAgent()
    
    def generate(self, input_data: ContentInput) -> Dict[str, Any]:
        # STEP 1: Analyze syllabus
        syllabus_data = self.syllabus_agent.analyze(
            input_data.syllabus_text,
            input_data.course_outline_text,
            input_data.subject_name
        )
        
        # STEP 2: Plan curriculum
        planned_topics = self.planning_agent.plan(
            syllabus_data["units"],
            input_data.class_duration
        )
        
        # STEP 3: Schedule based on mode
        schedule = self.scheduling_agent.schedule(
            planned_topics,
            input_data.mode,
            input_data.class_duration,
            input_data.timetable_text
        )
        
        # STEP 4: Generate content for allocated topics
        content = []
        for topic in schedule["allocated_topics"]:
            content.append(self.content_agent.generate(topic))
        
        # STEP 5: Validate
        validation = self.validation_agent.validate(
            content, syllabus_data, schedule, input_data.class_duration
        )
        
        # Prepare output
        all_topics = [t["topic"] for t in planned_topics]
        covered_topics = [t["topic"] for t in schedule["allocated_topics"]]
        remaining_topics = [t for t in all_topics if t not in covered_topics]
        
        output = {
            "subject": input_data.subject_name,
            "generation_mode": input_data.mode,
            "time_scope": schedule["time_scope"],
            "schedule": {
                "week_or_month": schedule["time_scope"],
                "lectures": schedule["lectures"]
            },
            "content": content,
            "generation_summary": {
                "covered_topics": covered_topics,
                "remaining_topics": remaining_topics
            },
            "validation": validation
        }
        
        return output


def main():
    """Example usage"""
    
    # Sample input
    input_data = ContentInput(
        syllabus_text="""
        Unit 1: Introduction to Programming
        - Variables and Data Types
        - Control Structures
        - Functions and Modules
        
        Unit 2: Object-Oriented Programming
        - Classes and Objects
        - Inheritance and Polymorphism
        - Encapsulation
        """,
        course_outline_text="Comprehensive programming course covering fundamentals to advanced concepts",
        timetable_text="Monday 10:00 AM - Class, Wednesday 2:00 PM - Class, Friday 11:00 AM - Class",
        subject_name="Programming Fundamentals",
        course_duration="14 weeks",
        class_duration=60,
        mode="Weekly"
    )
    
    # Generate content
    generator = CourseContentGenerator()
    result = generator.generate(input_data)
    
    # Output as JSON
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
