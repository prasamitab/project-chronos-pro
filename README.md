# Project Chronos: The AI Archeologist

**Student Name(s):** Prasamita Bangal
**Student ID(s):** SE23UMCS048

## Features

* **Interactive Web Interface:** A user-friendly UI built with Streamlit.
* **AI-Powered Text Reconstruction:** Translates cryptic slang into clear, modern English.
* **Deeper AI Analysis:** Estimates the text's time period (e.g., "Early 2000s") and slang category (e.g., "Gaming Slang").
* **Visual Context:** Automatically finds and displays a relevant historical image to provide an instant "aha!" moment of understanding.
* **Automated Source Linking:** Provides hyperlinks to articles and definitions for further reading.

## Project Description

Project Chronos is an "AI Archeologist" application that takes fragmented or obscure text from old internet sources. It uses the Google Gemini API to reconstruct the text into a clear, modern sentence and then performs an automated web search to find contextual sources that explain the original slang and cultural references.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/prasamitab/project-chronos-pro.git](https://github.com/prasamitab/project-chronos-pro.git)
    cd project-chronos-pro
    ```

2.  **Create and Activate a Virtual Environment:**
    *For macOS/Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *For Windows:*
    ```bash
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

1.  **Launch the Web Application**
    Run the following command in your terminal from the project's root directory:
    ```bash
    streamlit run app.py
    ```

2.  **Use the App**
    Your web browser will open with the application. Enter a piece of fragmented text into the input box and click the "Excavate ⛏️" button to see the full analysis.

    **Example Inputs:**
    * `smh at the top 8 drama. ppl need to chill. g2g, ttyl.`
    * `w00t! that n00b got pwned on Counter-Strike.`


## Future Plans

While Project Chronos is a fully functional tool, its potential can be expanded even further:

* **Browser Extension:** Develop a Chrome extension that allows users to highlight any text on any webpage, right-click, and get an instant reconstruction report.
* **Confidence Scoring:** Enhance the AI to provide a confidence score (e.g., "95% certain") for its reconstruction and analysis, adding a layer of scientific rigor.
* **Historical Trend Analysis:** Build functionality to analyze an entire forum thread or archive, visualizing how specific slang terms emerged and faded over time.
