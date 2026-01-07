# Complete Guide - AI Course Content Generator

## ✅ FINAL VERSION - Everything Working!

### What You Get

For each lecture topic, the system creates a **dedicated folder** containing:

```
Lecture_1_Variables_and_Data_Types/
├── Variables_and_Data_Types.pptx    (PowerPoint with real content)
├── Variables_and_Data_Types.pdf     (Comprehensive notes)
├── Variables_and_Data_Types.mp3     (Human-like voice - Microsoft neural TTS)
├── Variables_and_Data_Types.mp4     (Video with slides + audio)
└── slides/                          (Individual slide images)
```

---

## 🎯 Key Features

### 1. Real Educational Content
- Actual definitions (not placeholders)
- Working code examples
- Best practices from industry
- Real-world applications

### 2. Human-Like Voice
- **Microsoft Edge Neural TTS** (sounds like a real person!)
- Natural pauses and emphasis
- SSML tags for prosody
- Much better than robotic gTTS

### 3. Organized by Topic
- Each lecture in its own folder
- Easy to find and share
- Professional structure

### 4. Complete Package
- PowerPoint for presentations
- PDF for student notes
- Audio for listening/review
- Video for online learning

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install python-pptx reportlab edge-tts pyttsx3 pillow opencv-python pydub

# 2. Run generator
python generate_real_content.py

# 3. Check generated_files/ folder
```

---

## 🎙️ Voice Quality

### Microsoft Edge Neural TTS (Default)
- **Sounds like a real human teacher**
- Natural intonation and rhythm
- Automatic pauses and emphasis
- Free and unlimited
- Requires internet connection

### Fallback Options
1. **pyttsx3** - Offline voice (if no internet)
2. **gTTS** - Google TTS (last resort)

---

## 📁 File Organization

```
generated_files/
├── Lecture_1_Topic_Name/
│   ├── Topic_Name.pptx
│   ├── Topic_Name.pdf
│   ├── Topic_Name.mp3
│   ├── Topic_Name.mp4
│   └── slides/
│       ├── slide_00.png
│       ├── slide_01.png
│       └── ...
├── Lecture_2_Next_Topic/
│   └── ...
└── Subject_SUMMARY.pdf
```

---

## 🎨 Customization

Edit `generate_real_content.py`:

```python
# Change voice (line in file_generator.py)
voice = "en-US-GuyNeural"      # Male (default)
voice = "en-US-AriaNeural"     # Female
voice = "en-US-JennyNeural"    # Female (friendly)

# Change syllabus
my_syllabus = """
Unit 1: Your Topics
- Topic 1
- Topic 2
"""

# Change mode
my_mode = "Lecture-wise"  # One lecture
my_mode = "Weekly"        # One week
my_mode = "Monthly"       # One month
```

---

## 🔧 Technical Details

### Audio Generation Process
1. Takes conversational script
2. Adds SSML tags for natural speech
3. Uses Microsoft Edge Neural TTS
4. Adds pauses after sentences
5. Emphasizes important words
6. Slows down for questions

### Video Generation Process
1. Creates slide images (PNG)
2. Generates audio with neural voice
3. Uses OpenCV to create video
4. Combines with ffmpeg
5. Outputs MP4 file

---

## 📊 Content Quality

### Sample Audio Script
```
"Hello everyone! Welcome to today's lesson. I'm excited to teach you 
about Variables and Data Types. Let me start with a question - have 
you ever wondered how programs actually store and work with information? 
That's exactly what we're going to explore today..."
```

### With SSML Enhancement
```xml
Hello everyone!<break time="500ms"/> Welcome to today's lesson.<break time="500ms"/> 
I'm <emphasis level="strong">excited</emphasis> to teach you about Variables and 
Data Types.<break time="500ms"/> <prosody rate="0.9">Let me start with a question 
- have you ever wondered how programs actually store and work with information?
</prosody><break time="800ms"/>
```

---

## 🎓 Use Cases

1. **University Professors** - Generate semester content
2. **Online Course Creators** - Create video courses
3. **Corporate Training** - Develop training materials
4. **Self-Study** - Create personal learning materials

---

## 💡 Pro Tips

1. **Test with one lecture first** - Use "Lecture-wise" mode
2. **Listen to the audio** - Microsoft neural voice is MUCH better
3. **Customize the voice** - Try different neural voices
4. **Review content** - Always check before using in class
5. **Generate incrementally** - Week by week for better control

---

## 🆘 Troubleshooting

**Audio sounds robotic?**
- Make sure edge-tts is installed: `pip install edge-tts`
- Check internet connection (neural voices need internet)
- If offline, it falls back to pyttsx3

**Video not generating?**
- Install ffmpeg: https://ffmpeg.org/download.html
- Or use the video package (slides + audio separately)

**Files not organized in folders?**
- Check `file_generator.py` line 12: `self.use_topic_folders = True`

---

## 📦 Dependencies

```
edge-tts==6.1.9          # Microsoft neural voices (BEST)
pyttsx3==2.90            # Offline voice (fallback)
gtts==2.5.0              # Google TTS (last resort)
python-pptx==0.6.23      # PowerPoint generation
reportlab==4.0.7         # PDF creation
opencv-python==4.8.1.78  # Video generation
pydub==0.25.1            # Audio processing
pillow==10.1.0           # Image processing
```

---

## ✅ What's Working

- ✅ Real educational content (not placeholders)
- ✅ Human-like voice (Microsoft neural TTS)
- ✅ Organized by topic (folders for each lecture)
- ✅ Complete package (PPT, PDF, MP3, MP4)
- ✅ Conversational teaching style
- ✅ Natural pauses and emphasis
- ✅ Working video generation
- ✅ Professional quality output

---

## 🎉 Ready to Use!

```bash
python generate_real_content.py
```

Then check `generated_files/Lecture_1_*/` for your content!

**The audio now sounds like a real human teacher, not a robot!** 🎙️

---

Made with ❤️ for educators who need professional, human-sounding content
