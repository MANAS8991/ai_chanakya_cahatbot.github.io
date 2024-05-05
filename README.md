AI Chanakya ChatBot
This project implements an AI-powered chatbot using Streamlit, speech recognition, and language generation models from Hugging Face. The chatbot allows users to interact via voice input or text input, engaging in conversational exchanges powered by natural language understanding and generation.


Features
Voice interaction with the chatbot using speech recognition.
Conversational AI powered by Hugging Face's language models.
Text-to-speech functionality to provide audio responses.
Customizable conversational memory and model selection.
Setup
Install the required Python libraries:

pip install streamlit speech_recognition gtts groq langchain transformers
Set up environment variables:
Obtain a GROQ API key and set it as an environment variable:

export GROQ_API_KEY="your_groq_api_key_here"
Run the Streamlit app locally:

streamlit run app.py
Usage
Choose a language model (LLM) and conversational memory length using the sidebar options.
Speak into the microphone or type a question/query into the text area to interact with the chatbot.
Click the "Speak" button to use voice input (requires microphone access).
Demo
Watch the Web App Demo Video

Screenshots

Caption: Chatting with the AI Chanakya ChatBot.


Caption: Selecting a language model and conversational memory length.

Credits
Streamlit: Interactive web app framework for building ML applications.
Hugging Face Transformers: Library for state-of-the-art NLP models and pipelines.
SpeechRecognition: Library for speech recognition in Python.
gTTS (Google Text-to-Speech): Library for text-to-speech conversion.
GROQ: Chatbot service for conversation APIs.
LangChain: Library for building conversational AI systems.
License
This project is licensed under the MIT License - see the LICENSE file for details.
