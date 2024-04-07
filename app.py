import streamlit as st
import os
import speech_recognition as sr
from gtts import gTTS
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.environ["GROQ_API_KEY"]

def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write("<h2 style='color: #00FFFF;'>Listening...</h2>", unsafe_allow_html=True)
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio, language="en-US")
        st.write(f"<h2 style='color: #ff6347;'>You said:</h2><p style='color: #FFFFFF;'>{user_input}</p>", unsafe_allow_html=True)
        return user_input
    except sr.UnknownValueError:
        st.write("<h2 style='color: #f00;'>Sorry, I didn't understand that. Please try again.</h2>", unsafe_allow_html=True)
    except sr.RequestError as e:
        st.write(f"<h2 style='color: #f00;'>Error: {e}</h2>", unsafe_allow_html=True)

    return None

def main():
    st.title("AI Chanakya ChatBot")

    # Add customization options to the sidebar
    st.sidebar.title('Select an LLM')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    # Session state variable
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model
    )
    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    # Display chatbot photo
    st.image("AI Chanakya.png", caption="AI Chanakya ChatBot", use_column_width=True)

    if st.button("Speak"):
        user_input = voice_to_text()
        if user_input:
            response = conversation(user_input)
            message = {'human': user_input, 'AI': response['response']}
            st.session_state.chat_history.append(message)
            st.write(f"<h2 style='color: #FF69B4;'>Chatbot:</h2><p style='color: #FFFFFF;'>{response['response']}</p>", unsafe_allow_html=True)

            # Text-to-speech
            tts = gTTS(response['response'], lang="en")
            tts.save("response.mp3")

            # Automatic playback of the audio response
            st.audio("response.mp3", format="audio/mp3", start_time=0)

    user_question = st.text_area("Ask a question:")
    if user_question:
        response = conversation(user_question)
        message = {'human': user_question, 'AI': response['response']}
        st.session_state.chat_history.append(message)
        st.write(f"<h2 style='color: #FF69B4;'>Chatbot:</h2><p style='color:  #FFFFFF;'>{response['response']}</p>", unsafe_allow_html=True)

        # Text-to-speech
        tts = gTTS(response['response'], lang="en")
        tts.save("response.mp3")

        # Automatic playback of the audio response
        st.audio("response.mp3", format="audio/mp3", start_time=0)

if __name__ == "__main__":
    main()
