import streamlit as st
import openai

# Set up OpenAI API key
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")
openai.api_key = api_key

# Home Page
st.title("🐍 Python Tutor for Kids")
st.write("""
Welcome to the Python Tutor! This app helps you learn Python in a fun and interactive way. 
You can ask questions, solve coding challenges, and even customize your AI tutor!
""")

# Customize AI Tutor
st.header("🎨 Customize Your AI Tutor")
tutor_character = st.selectbox("Choose your tutor character:", ["Robot", "Dinosaur", "Superhero", "Pirate"])
st.write(f"Your AI tutor is a {tutor_character}! 🎉")

# Chat with AI Tutor
st.header("💬 Chat with Your AI Tutor")
user_input = st.text_input("Ask a question or type 'help' for a lesson:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a friendly {tutor_character} who teaches Python to kids."},
            {"role": "user", "content": user_input}
        ]
    )
    st.write(response['choices'][0]['message']['content'])

# Interactive Code Editor
st.header("👩‍💻 Write and Run Python Code")
code = st.text_area("Write your Python code here:", height=200)
if st.button("Run Code"):
    try:
        exec(code)
    except Exception as e:
        st.error(f"Error: {e}")

# Homework Assignment
st.header("📚 Homework")
st.write("Write a Python program to print numbers from 1 to 10.")
if st.button("Show Solution"):
    st.code("""
for i in range(1, 11):
    print(i)
    """)
