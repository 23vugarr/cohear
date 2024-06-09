from navigation import make_sidebar
import streamlit as st

make_sidebar()

st.session_state.quiz_state = 'start'

# Define navigation function for quiz
def navigate_to(page):
    st.session_state.quiz_state = page

# CSS for styling buttons with images
st.markdown(
    """
    <style>
    .quiz-button {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 250px;
        height: 250px;
        background-color: #f0f0f0;
        border: 1px solid #ddd;
        border-radius: 8px;
        margin: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-align: center;
    }

    .quiz-button img {
        width: 200px;
        height: 200px;
        object-fit: cover;
        border-radius: 50%;
    }

    .quiz-button:hover {
        background-color: #e0e0e0;
    }

    .quiz-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Define the quiz question and answers
question = "What is the sound of this ?"
answers = [
    {"label": "Bird", "image": "images/bird.jpg", "is_correct": False},
    {"label": "Rain", "image": "images/rain.png", "is_correct": False},
    {"label": "Siren", "image": "images/siren.jpg", "is_correct": True},
    {"label": "Dog barking", "image": "images/dog.webp", "is_correct": False},
]

# Render the quiz page
if st.session_state.quiz_state == 'start':
    st.write("# Weekly Quiz")
    st.write(question)

    # Container for the buttons
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    
    st.audio("images/police-operation-siren-144229.mp3")
    for answer in answers:
        button_key = f"button_{answer['label']}"
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(answer['image'], use_column_width=True)
            with col2:
                if st.button(answer['label'], key=button_key):
                    if answer['is_correct']:
                        
                        st.write("Correct!")
                    else:
                        st.write("Incorrect!")
    st.markdown('</div>', unsafe_allow_html=True)

# Handle other quiz states if necessary
elif st.session_state.quiz_state == 'next':
    st.write("# Next Question Page")
    # Add content for the next question here
    if st.button("Back to Quiz"):
        navigate_to('start')
