# 🎓 Faculty Lesson Planner - AI Course Content Generator

**Transform your syllabus into complete teaching materials in seconds!**

Generate PowerPoint presentations, PDF notes, audio lectures, and videos with human-like voice - all from your course syllabus.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Features

- 🎯 **Real Educational Content** - Actual definitions, working code examples, industry best practices
- 🎙️ **Human-Like Voice** - Microsoft Edge Neural TTS (sounds like a real teacher!)
- 🎨 **Beautiful Slides** - Aesthetic gradient backgrounds, modern design
- 📦 **Complete Package** - PPT, PDF, MP3, MP4 for each lecture
- 📁 **Organized Output** - Each lecture in its own folder
- ⚡ **Fast Generation** - 30 seconds per lecture topic

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install python-pptx reportlab edge-tts pyttsx3 pillow opencv-python pydub
```

### 2. Run Generator

```bash
python generate_real_content.py
```

### 3. Check Output

```bash
cd generated_files/Lecture_1_*/
```

---

## 📁 What You Get

For each lecture topic:

```
Lecture_1_Variables_and_Data_Types/
├── Variables_and_Data_Types.pptx    # PowerPoint presentation
├── Variables_and_Data_Types.pdf     # Comprehensive notes
├── Variables_and_Data_Types.mp3     # Human-like audio lecture
├── Variables_and_Data_Types.mp4     # Video with slides + audio
└── slides/                          # Individual slide images
    ├── slide_00.png
    ├── slide_01.png
    └── ...
```

---

## 🎨 Slide Design

- **Gradient Backgrounds** - Purple to blue professional look
- **Modern Layout** - Clean, readable design
- **High Contrast** - White text on colored backgrounds
- **Professional Elements** - Shadows, decorative bars, bullet circles

---

## 🎙️ Audio Quality

- **Microsoft Edge Neural TTS** - Sounds like a real human teacher
- **Natural Speech** - Proper pacing, intonation, emphasis
- **No Robotic Voice** - Clean, professional audio
- **Multiple Voice Options** - Male/Female voices available

---

## 📝 Customization

### Change Your Syllabus

Edit `generate_real_content.py`:

```python
my_syllabus = """
Unit 1: Your Topics
- Topic 1
- Topic 2
"""

my_subject = "Your Subject Name"
my_mode = "Weekly"  # or "Lecture-wise" or "Monthly"
```

### Change Voice

Edit `file_generator.py` (line ~220):

```python
voice = "en-US-GuyNeural"      # Male (default)
voice = "en-US-AriaNeural"     # Female
voice = "en-US-JennyNeural"    # Female (friendly)
```

---

## 📚 Documentation

- **[FINAL_VERSION.md](FINAL_VERSION.md)** - Complete feature list
- **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** - Detailed usage guide
- **[RUN_THIS.txt](RUN_THIS.txt)** - Quick reference
- **[WHATS_FIXED.md](WHATS_FIXED.md)** - Changelog

---

## 🎯 Use Cases

- **University Professors** - Generate semester content
- **Online Course Creators** - Create video courses
- **Corporate Training** - Develop training materials
- **Tutoring** - Supplementary learning materials

---

## 🔧 Requirements

```
Python 3.8+
edge-tts==6.1.9          # Microsoft neural voices
python-pptx==0.6.23      # PowerPoint generation
reportlab==4.0.7         # PDF creation
opencv-python==4.8.1.78  # Video generation
pydub==0.25.1            # Audio processing
pillow==10.1.0           # Image processing
pyttsx3==2.90            # Offline voice (fallback)
gtts==2.5.0              # Google TTS (fallback)
```

---

## 💡 Generation Modes

| Mode | Generates | Best For |
|------|-----------|----------|
| **Lecture-wise** | 1 lecture | Testing, single class |
| **Weekly** | 1 week | Week-by-week planning |
| **Monthly** | 1 month | Semester planning |

---

## 🌐 Web Interface (Optional)

```bash
pip install flask
python app.py
```

Open: http://localhost:5000

---

## 🆘 Troubleshooting

**Audio sounds robotic?**
- Install edge-tts: `pip install edge-tts`
- Check internet connection (neural voices need internet)

**Video not generating?**
- Install ffmpeg: https://ffmpeg.org/download.html
- Or use the video package (slides + audio separately)

**Files not organized in folders?**
- Check `file_generator.py` line 12: `self.use_topic_folders = True`

---

## 📊 Sample Output

### Content Quality:
- ✅ Real definitions (200+ words)
- ✅ Working code examples (5+ per topic)
- ✅ Best practices (industry standards)
- ✅ Real-world applications
- ✅ Common mistakes to avoid

### File Sizes:
- PowerPoint: ~35 KB
- PDF: ~4 KB
- Audio: ~2-3 MB
- Video: ~4-6 MB

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

MIT License - Free to use for educational purposes

---

## 🙏 Acknowledgments

Built with:
- Microsoft Edge TTS for natural voice
- python-pptx for PowerPoint generation
- ReportLab for PDF creation
- OpenCV for video generation

---

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for educators worldwide**

*Transform your teaching with AI-powered content generation*
