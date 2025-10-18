# main.py
import os
import sys
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro-latest')

def search_for_context(query_text, search_type='text'):
    """Searches the web for text links or a single image URL."""
    try:
        search_api_key = os.getenv("GOOGLE_API_KEY")
        search_engine_id = os.getenv("SEARCH_ENGINE_ID")
        url = "https://www.googleapis.com/customsearch/v1"
        params = { 'key': search_api_key, 'cx': search_engine_id, 'q': query_text }

        if search_type == 'image':
            params['searchType'] = 'image'
            params['num'] = 1
        else:
            params['num'] = 3

        response = requests.get(url, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        if search_type == 'image':
            return search_results.get('items', [{}])[0].get('link')
        else:
            return [item['link'] for item in search_results.get('items', [])]
    except Exception as e:
        print(f"Web search failed: {e}")
        return None if search_type == 'image' else []

def get_time_period(original_fragment):
    """Asks the AI to estimate the time period of the slang."""
    prompt = f"""Based on the slang and context in the following text, what is the most likely time period it is from? Provide a short answer, like "Early 2000s" or "Late 1990s". Original Fragment: "{original_fragment}" """
    response = model.generate_content(prompt)
    return response.text.strip()

def get_slang_category(original_fragment):
    """Asks the AI to categorize the slang."""
    prompt = f"""
    Categorize the slang or cultural reference in the following text.
    Use categories like "Gaming Slang," "Chat Acronyms," "Social Media Jargon," or "General Internet Slang."
    Provide only the category name.

    Original Fragment: "{original_fragment}"
    """
    response = model.generate_content(prompt)
    return response.text.strip()


def generate_report(original_fragment):
    """Generates the full report with text, links, time period, and an image."""
    try:
        # AI Reconstruction
        reconstruction_prompt = f"""Your sole task is to rephrase the following fragmented text from early internet culture into a single, complete, modern English sentence. Directly translate the slang and meaning. Do NOT add any analysis or preamble. Just provide the rephrased sentence. Original Fragment: "{original_fragment}" """
        reconstructed_text = model.generate_content(reconstruction_prompt).text.strip()
        
        # AI Keyword Extraction
        keyword_prompt = f"""From the following text, extract the key slang terms and unique cultural references. Return them as a simple, comma-separated list. Example: for "w00t! that n00b got pwned on Counter-Strike", return "w00t, n00b, pwned, Counter-Strike". Original Fragment: "{original_fragment}" """
        search_query = model.generate_content(keyword_prompt).text.strip()
        
        # Deeper Analysis
        time_period = get_time_period(original_fragment)
        slang_category = get_slang_category(original_fragment) 
        
        # Web & Image Search
        contextual_links = search_for_context(search_query, search_type='text')
        context_image_url = search_for_context(search_query, search_type='image')
        
        return {
            "original": original_fragment,
            "reconstructed": reconstructed_text,
            "links": contextual_links,
            "period": time_period,
            "category": slang_category,
            "image": context_image_url
        }
    except Exception as e:
        return {"error": str(e)}

# This part allows you to still run from the command line if needed
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your fragmented text here>\"")
    else:
        report = generate_report(sys.argv[1])
        print(report)
