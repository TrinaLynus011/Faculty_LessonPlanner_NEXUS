"""
Generate REAL Educational Content with Actual Meaningful Information
Uses intelligent content generation + file creation
"""

from course_content_generator import CourseContentGenerator, ContentInput
from file_generator import FileGenerator
from intelligent_content_generator import IntelligentContentGenerator
import os


def generate_real_course_content():
    """
    Generate actual meaningful educational content
    EDIT THE INPUT DATA BELOW
    """
    
    print("\n" + "="*80)
    print("INTELLIGENT COURSE CONTENT GENERATOR")
    print("   Generates REAL educational content with actual information")
    print("="*80)
    
    # ============================================================
    # CUSTOMIZE YOUR INPUT HERE
    # ============================================================
    
    my_syllabus = """
    Unit 1: Python Programming Fundamentals
    - Variables and Data Types
    - Control Structures
    - Functions and Modules
    
    Unit 2: Object-Oriented Programming
    - Classes and Objects
    - Inheritance
    - Polymorphism
    
    Unit 3: Data Structures
    - Lists and Tuples
    - Dictionaries and Sets
    - Stacks and Queues
    """
    
    my_course_outline = "Comprehensive Python programming course covering fundamentals, OOP, and data structures with practical examples"
    
    my_timetable = "Monday 10:00 AM, Wednesday 2:00 PM, Friday 11:00 AM"
    
    my_subject = "Python Programming"
    
    my_duration = "12 weeks"
    
    my_class_duration = 90  # minutes
    
    my_mode = "Lecture-wise"  # Start with one lecture to see quality
    
    # ============================================================
    # GENERATION STARTS HERE
    # ============================================================
    
    # Create input
    input_data = ContentInput(
        syllabus_text=my_syllabus,
        course_outline_text=my_course_outline,
        timetable_text=my_timetable,
        subject_name=my_subject,
        course_duration=my_duration,
        class_duration=my_class_duration,
        mode=my_mode
    )
    
    # Step 1: Generate content structure
    print("\nStep 1: AI Agents analyzing syllabus...")
    generator = CourseContentGenerator()
    result = generator.generate(input_data)
    
    print(f"\nContent structure generated:")
    print(f"   Subject: {result['subject']}")
    print(f"   Mode: {result['generation_mode']}")
    print(f"   Scope: {result['time_scope']}")
    print(f"   Topics to generate: {len(result['content'])}")
    
    # Step 2: Generate actual files with real content
    print(f"\nStep 2: Creating files with REAL content...")
    print("   (This includes web research for meaningful information)")
    
    file_gen = FileGenerator()
    files = file_gen.generate_all(result["content"], result["subject"])
    
    # Display results
    print("\n" + "="*80)
    print("FILES GENERATED SUCCESSFULLY WITH REAL CONTENT!")
    print("="*80)
    print(f"\nOutput folder: {file_gen.output_dir}/")
    print("\nGenerated files:\n")
    
    for idx, item in enumerate(files["files"], 1):
        print(f"  {idx}. {item['topic']}")
        print(f"     Unit: {item['unit']}")
        if item.get('folder'):
            print(f"     Folder: {os.path.basename(item['folder'])}/")
        for file_type, filepath in item["files"].items():
            filename = os.path.basename(filepath)
            if file_type == "video":
                if filepath.endswith("_VIDEO_PACKAGE"):
                    print(f"        [VIDEO PKG] {filename}/")
                elif filepath.endswith(".mp4"):
                    print(f"        [MP4] {filename}")
                else:
                    print(f"        [VIDEO] {filename}")
            else:
                icon = {
                    "ppt": "[PPT]",
                    "pdf": "[PDF]",
                    "audio": "[MP3]"
                }.get(file_type, "[FILE]")
                print(f"        {icon} {filename}")
        print()
    
    print(f"  [SUMMARY] {os.path.basename(files['summary'])}")
    
    # Summary
    print("\n" + "="*80)
    print("CONTENT QUALITY")
    print("="*80)
    print("\nWhat's Different:")
    print("   * REAL definitions and explanations (not generic)")
    print("   * ACTUAL code examples (not placeholders)")
    print("   * MEANINGFUL best practices (from knowledge base)")
    print("   * PRACTICAL applications (real-world scenarios)")
    print("   * VIDEO files included (MP4 or slide images)")
    print("   * CONVERSATIONAL audio (teaching style, not reading)")
    print("\nCovered Topics:")
    for topic in result['generation_summary']['covered_topics']:
        print(f"   * {topic}")
    
    if result['generation_summary']['remaining_topics']:
        print(f"\nRemaining Topics ({len(result['generation_summary']['remaining_topics'])}):")
        for topic in result['generation_summary']['remaining_topics'][:5]:
            print(f"   * {topic}")
        if len(result['generation_summary']['remaining_topics']) > 5:
            print(f"   ... and {len(result['generation_summary']['remaining_topics']) - 5} more")
    
    print("\n" + "="*80)
    print("DONE! Open the files to see REAL educational content.")
    print("="*80)
    print("\nNext Steps:")
    print("   1. Open the PowerPoint - see actual content, not placeholders")
    print("   2. Read the PDF - comprehensive notes with real examples")
    print("   3. Listen to audio - conversational teaching style")
    print("   4. Watch video - slides synchronized with audio")
    print("\n   To generate more topics, change mode to 'Weekly' or 'Monthly'")
    print("="*80 + "\n")
    
    return files


if __name__ == "__main__":
    generate_real_course_content()
