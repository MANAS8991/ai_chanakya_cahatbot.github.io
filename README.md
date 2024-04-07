# ai_chanakya_cahatbot.github.io

AI Chanakya ChatBot
AI Chanakya ChatBot is an interactive voice and text-based chatbot powered by Groq Langchain technology. It allows users to ask questions and engage in conversations with the chatbot using both speech input and text input.

Features
Voice Recognition: Users can speak to the chatbot using their microphone, and the chatbot will transcribe the speech into text.
Text Input: Users can also type their questions or messages directly into the text input area.
Conversation History: The chatbot maintains a conversation history, allowing users to see previous interactions.
Customization: Users can customize the chatbot's behavior by selecting different language models and conversational memory lengths.
Usage
Select Language Model: Choose a language model from the sidebar to customize the chatbot's behavior.
Ask a Question: Type your question in the text input area or click the "Speak" button to ask a question using voice input.
Interact with the Chatbot: The chatbot will provide responses to your questions and engage in conversation.
View Conversation History: You can see the conversation history in the main panel, including your questions and the chatbot's responses.
Installation

To run the AI Chanakya ChatBot locally, follow these steps:

Clone the repository: git clone https://github.com/MANAS8991/ai_chanakya_cahatbot.github.io.git

Navigate to the project directory: cd ai-chanakya-chatbot

Install dependencies: pip install -r requirements.txt

Set up environment variables:
Obtain a Groq API key and set it as GROQ_API_KEY in a .env file.

Run the app: streamlit run app.py

Technologies Used
Streamlit: Web framework for building interactive web applications.
SpeechRecognition: Library for performing speech recognition in Python.
gTTS (Google Text-to-Speech): Python library and CLI tool to interface with Google Translate's text-to-speech API.
Groq Langchain: API for generating text-based responses using Groq language models.
