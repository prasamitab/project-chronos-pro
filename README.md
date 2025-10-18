# Project Chronos: The AI Archeologist

**Student Name(s):** Prasamita Bangal
**Student ID(s):** SE23UMCS048

## Project Description

Project Chronos is an "AI Archeologist" application that takes fragmented or obscure text from old internet sources. It uses the Google Gemini API to reconstruct the text into a clear, modern sentence and then performs an automated web search to find contextual sources that explain the original slang and cultural references.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/prasamitab/project-chronos
    cd project-chronos
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up API Keys:**
    Create a file named `.env` in the root of the project folder and add your API keys in the following format:
    ```
    GEMINI_API_KEY="AIzaSyBISXh-4QFcNuHj99eeMS7Rz6KQ5AuUNfs"
    GOOGLE_API_KEY="AIzaSyCvTH5qfpmBAnA8FSsIkQL3N2NVRgQOtdU"
    SEARCH_ENGINE_ID="56f1de97ea0d041a4"
    ```

## Usage Guide

Run the application from your terminal by providing the fragmented text in quotes as a command-line argument.

**Example Command:**
```bash
python main.py "smh at the top 8 drama. ppl need to chill. g2g, ttyl."
python main.py "w00t! that n00b got pwned on Counter-Strike."
