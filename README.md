# AI Voice Mock Interview Studio 🎙️🤖

An interactive, responsive, AI-powered web application designed to help job applicants prepare for technical and behavioral interviews. By simulating a real-world verbal interview experience, it provides users with custom-generated questions, real-time voice-to-text recording, browser-based speech output, and deep, metric-driven AI feedback.

---

## 🌟 Key Features

* **📄 Dynamic Resume Parsing:** Extract details (Name, Skills, Projects, Experience, Education) from uploaded PDF and DOCX files automatically.
* **🧠 Context-Locked AI Question Generation:** Gemini analyzes the candidate's parsed resume details and generates structured interview questions tailored specifically to their background and target role.
* **🔊 Interactive Audio Playback (TTS):** Automatically reads each question aloud inside the candidate's browser using HTML5 `SpeechSynthesis`.
* **🎙️ Voice Recording & Live Transcription (STT):** Records the candidate's voice answer, performs voice-to-text transcription, and prints the result instantly in an editable text area.
* **📊 Granular Performance Evaluation:** Gemini evaluates the candidate's answers based on Communication, Technical Knowledge, Confidence, Completeness, and Grammar, scoring them out of 100 and providing a study roadmap.

---

## 🛠️ Technology Stack

* **Frontend & Framework:**
  * **Streamlit (v1.36.0+):** Utilized for fast UI rendering, layouts, and session state management.
  * **HTML5 Web Speech API (SpeechSynthesis):** Provides client-side, zero-dependency, and free Text-to-Speech (TTS) audio.
* **Speech-to-Text (STT):**
  * **streamlit-mic-recorder:** Renders browser mic interfaces. It transfers audio streams as WAV files to the backend where it interfaces with the free Google Speech Recognition Web API.
* **AI Engine:**
  * **google-genai (v0.6.0+):** The official, modern Google GenAI Python SDK. Used to connect to Gemini.
  * **Gemini 3.5 Flash (`models/gemini-3.5-flash`):** Serves as the centralized AI model for question generation and multi-metric interview evaluation.
* **Resume Parser:**
  * **pdfplumber:** Extracted line-by-line structured text from PDF documents.
  * **python-docx:** Extracted text paragraphs from DOCX documents.
* **Configuration & Styling:**
  * **python-dotenv:** Loads credentials and settings from `.env` files.
  * **Vanilla CSS:** Applied via Streamlit markdown injections to provide a dark-mode glassmorphism theme with premium badges, button hovers, and custom grids.

---

## 📂 Project Structure

```text
AI Voice Mock Interview Platform/
├── .env                         # Local environment configuration for API secrets
├── .env.example                 # Environment template for model and API configurations
├── .gitignore                   # Excludes venv, private keys, local uploads, and cache folders
├── app.py                       # Main application script and page router
├── requirements.txt             # Centralized list of core package dependencies
├── .streamlit/
│   └── config.toml              # Streamlit client settings (hides default navigation)
├── assets/                      # Media, icons, and static assets
├── components/
│   └── __init__.py              # Initializer for reusable components package
├── pages/
│   ├── __init__.py              # Initializer for pages package
│   ├── feedback.py              # Page displaying AI evaluation dashboard
│   ├── home.py                  # Landing page with feature showcases
│   ├── interview.py             # Active voice-guided interview session dashboard
│   └── resume_upload.py         # Resume parsing and setup page
├── services/
│   ├── __init__.py              # Initializer for services package
│   ├── ai/
│   │   ├── __init__.py          # Initializer for AI services
│   │   ├── gemini_service.py    # Main Gemini question & evaluation handler
│   │   └── test_gemini.py       # Helper script to validate model availability
│   ├── parsing/
│   │   ├── __init__.py          # Initializer for resume parsing
│   │   ├── constants.py         # Parsing patterns and section heading aliases
│   │   ├── resume_parser.py     # Main parser coordinate logic
│   │   ├── section_parser.py    # Section mapping and detail heuristics
│   │   └── text_extractors.py   # PDF / DOCX byte readers
│   └── voice/
│       ├── __init__.py          # Initializer for voice services
│       ├── session.py           # In-memory session logging utilities
│       └── tts.py               # HTML/JS browser Text-To-Speech utility
├── uploads/
│   └── .gitkeep                 # Preserves the directory structure for files
└── utils/
    ├── __init__.py              # Initializer for utils package
    ├── formatting.py            # Safe data casting and name-scrubbing utils
    ├── settings.py              # Environment variable loading settings
    └── ui.py                    # Custom dark-theme CSS and global UI wrappers
```

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/artistic-engineer-13/test1.git
cd test1
```

### 2. Create and Activate a Virtual Environment
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```
Open `.env` and fill in your Gemini API Key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_MODEL=models/gemini-3.5-flash
```

### 5. Run the Application
```bash
streamlit run app.py
```
Open the URL (typically `http://localhost:8501`) in your browser to start the app.

---

## 📝 License

This project is open-source and available under the MIT License.
