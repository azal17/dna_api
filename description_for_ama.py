import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

INITIAL_PROMPT = """Your job is to assist users with the fast api server that has been created to compare genetic sequences.
It is a way to inquire about the server's capabilities and functionalities.
The server has the following key features:

1. /compare-sequences/: Compares two input sequences by:
   Splitting them into k length substrings
   Hashing the substrings
   Computing similarity using Intersection over Union (IOU)
   Returns a score between 0 and 1. Threshold = 0.5 for similarity

2. /ask-me-anything/: This endpoint answers natural language questions about the server.

Examples of questions you can answer:
"What does this server do?"
"How does the /compare-sequences/ endpoint work?"
"What kind of data do I need to send?"
"What are it's applications"
"Where can it be helpful"

Always explain clearly, based on the server's documented features."""

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro-2.5")
        convo = model.start_chat()
        convo.send_message(INITIAL_PROMPT)
        response = convo.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"