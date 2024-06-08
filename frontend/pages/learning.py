from navigation import make_sidebar
import streamlit as st

make_sidebar()

def first_quiz():
    st.header("1. Match the voice")
    st.image('images/rain.png')
    st.audio('images/rain_voice.m4a')
    if st.button("Next"):
        st.session_state.current_quiz = "second_quiz"

def second_quiz():
    st.header("2. Match the voice")
    st.image('images/bird.jpg')
    st.audio('images/bird.weba')
    if st.button("Next"):
        st.session_state.current_quiz = "success" 

def success_page():
    st.success("Congrats!!!")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("restart"):
            st.session_state.current_quiz = "first_quiz"
    with col2:
        if st.button("back to main page"):
            st.switch_page("pages/dashboard.py")
    with col3:
        pass
     

if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = "first_quiz"

if st.session_state.current_quiz == "first_quiz":
    first_quiz()
elif st.session_state.current_quiz == "second_quiz":
    second_quiz()
elif st.session_state.current_quiz == "success":
    success_page()
