
import os
import sys
import requests
import google.generativeai as genai
from dotenv import load_dotenv

def search_for_context(query_text):
    """Searches the web for context and returns the top 3 links."""
    print(f"🔎 Searching for context with query: \"{query_text}\"")
    try:
        search_api_key = os.getenv("GOOGLE_API_KEY")
        search_engine_id = os.getenv("SEARCH_ENGINE_ID")
        
        if not search_api_key or not search_engine_id:
            raise ValueError("Google Search API Key or Engine ID not found in .env file.")

        url = "https://www.googleapis.com/customsearch/v1"
        params = { 'key': search_api_key, 'cx': search_engine_id, 'q': query_text, 'num': 3 }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        links = [item['link'] for item in search_results.get('items', [])]
        return links

    except Exception as e:
        print(f"❌ Web search failed: {e}")
        return []

def main():
    load_dotenv()

    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"❌ Error configuring Gemini API: {e}")
        return

    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your fragmented text here>\"")
        return
    
    original_fragment = sys.argv[1]
    model = genai.GenerativeModel('gemini-pro-latest')

    try:
        # --- STEP 1: AI Reconstruction ---
        print("⏳ Reconstructing text with Gemini...")
        reconstruction_prompt = f"""
        Your sole task is to rephrase the following fragmented text from early internet culture into a single, complete, modern English sentence.
        Directly translate the slang and meaning. Do NOT add any analysis, preamble, or explanation.
        Just provide the rephrased sentence and nothing more.

        Original Fragment: "{original_fragment}"
        """
        response = model.generate_content(reconstruction_prompt)
        reconstructed_text = response.text.strip()
        
        # --- STEP 2: AI Keyword Extraction for a Better Search ---
        keyword_prompt = f"""
        From the following text, extract the key slang terms and unique cultural references that need explaining.
        Return them as a simple, comma-separated list.
        
        Example: for "w00t! that n00b got pwned on Counter-Strike", return "w00t, n00b, pwned, Counter-Strike".
        
        Original Fragment: "{original_fragment}"
        """
        keyword_response = model.generate_content(keyword_prompt)
        search_query = keyword_response.text.strip()
        
        # --- STEP 3: Web Search using Keywords ---
        contextual_links = search_for_context(search_query)
        
        # --- STEP 4: Display the Final Report ---
        print("\n\n--- RECONSTRUCTION REPORT ---")
        print(f"\n[Original Fragment]\n> {original_fragment}")
        print(f"\n[AI-Reconstructed Text]\n> {reconstructed_text}")
        print("\n[Contextual Sources]")
        if contextual_links:
            for link in contextual_links:
                print(f"* {link}")
        else:
            print("No sources found.")

    except Exception as e:
        print(f"\n❌ An error occurred during the process: {e}")

if __name__ == "__main__":
    main()



