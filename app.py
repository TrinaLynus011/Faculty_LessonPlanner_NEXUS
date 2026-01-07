"""
Enhanced Web App - Generates actual files (PPT, PDF, Audio)
Similar to ChatGPT and NotebookLM
"""

from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from course_content_generator import CourseContentGenerator, ContentInput
from file_generator import FileGenerator
import os
import zipfile
from datetime import datetime

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        
        # Create input
        input_data = ContentInput(
            syllabus_text=data['syllabus_text'],
            course_outline_text=data['course_outline_text'],
            timetable_text=data['timetable_text'],
            subject_name=data['subject_name'],
            course_duration=data['course_duration'],
            class_duration=int(data['class_duration']),
            mode=data['mode']
        )
        
        # Generate content
        generator = CourseContentGenerator()
        result = generator.generate(input_data)
        
        # Generate files
        file_gen = FileGenerator()
        files = file_gen.generate_all(result["content"], result["subject"])
        
        # Prepare response
        response = {
            "success": True,
            "subject": result["subject"],
            "mode": result["generation_mode"],
            "time_scope": result["time_scope"],
            "covered_topics": result["generation_summary"]["covered_topics"],
            "remaining_topics": result["generation_summary"]["remaining_topics"],
            "files": []
        }
        
        # Add file info
        for item in files["files"]:
            file_info = {
                "topic": item["topic"],
                "unit": item["unit"],
                "downloads": {
                    "ppt": f"/download/{os.path.basename(item['files']['ppt'])}",
                    "pdf": f"/download/{os.path.basename(item['files']['pdf'])}",
                    "audio": f"/download/{os.path.basename(item['files']['audio'])}"
                }
            }
            response["files"].append(file_info)
        
        response["summary_pdf"] = f"/download/{os.path.basename(files['summary'])}"
        response["download_all"] = f"/download-all/{result['subject']}"
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    """Download individual file"""
    return send_from_directory('generated_files', filename, as_attachment=True)

@app.route('/download-all/<subject>')
def download_all(subject):
    """Download all files as ZIP"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"{subject}_{timestamp}.zip"
    zip_path = os.path.join('generated_files', zip_filename)
    
    # Create ZIP
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk('generated_files'):
            for file in files:
                if not file.endswith('.zip'):
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, file)
    
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🎓 COURSE CONTENT GENERATOR - File Generation System")
    print("="*70)
    print("\n✨ Features:")
    print("  • Generates actual PPT, PDF, and Audio files")
    print("  • Similar to ChatGPT and NotebookLM output")
    print("  • Download individual files or all as ZIP")
    print("\n🌐 Server starting...")
    print("  Open: http://localhost:5000")
    print("\n⌨️  Press Ctrl+C to stop")
    print("="*70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
