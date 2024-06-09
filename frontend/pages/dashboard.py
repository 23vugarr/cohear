from navigation import make_sidebar
import streamlit as st

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard.py'

# Define navigation function
def navigate_to(page):
    st.session_state.page = page

# Render content based on the current page
if st.session_state.page == 'dashboard.py':
    make_sidebar()
    st.write('# Your Dashboard 💻')
    st.write('## Week 1')

    st.markdown(
        """
        <style>
        /* Specific button colors */
        .green-button {
            background-color: green !important;
            color: white !important;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 10px;
            width: 100%;
        }

        .yellow-button {
            background-color: yellow !important;
            color: black !important;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 10px;
            width: 100%;
        }

        .red-button {
            background-color: red !important;
            color: white !important;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 10px;
            width: 100%;
        }

        /* Expander styling */
        .stExpander {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 10px;
        }

        /* Align button columns */
        .stColumn {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def create_lesson(lesson_title, sound_list, button_label, button_color_class, page_to_navigate):
        instructionCol, buttonCol = st.columns([5, 1])
        with instructionCol:
            with st.expander(lesson_title):
                for sound in sound_list:
                    st.write(sound)
        with buttonCol:
            if st.button(button_label, key=lesson_title):
                if page_to_navigate == "lesson_1_done" or page_to_navigate == "lesson_2_start":
                    st.switch_page("./pages/learning.py")
                elif page_to_navigate == "quiz":
                    st.switch_page("./pages/quiz.py")

    # Week 1 Lessons
    create_lesson("Lesson 1: Nature Sounds", ["Nature Sounds", "City Sounds", "Child sounds"], "Done", "green-button", "lesson_1_done")
    create_lesson("Lesson 2: River and Waterfall Sounds", ["River and Waterfall Sounds", "Wind Sounds", "Rain sounds"], "Start", "yellow-button", "lesson_2_start")
    create_lesson("Weekly quiz 1", ["Traffic Sounds", "Sirens", "People Talking"], "Locked", "red-button", "quiz")

    st.write('## Week 2')
    create_lesson("Lesson 1: Musical Instruments", ["Piano Sounds", "Guitar Sounds", "Drums sounds"], "Locked", "red-button", "none")
    create_lesson("Lesson 2: Household Sounds", ["Doorbell Sounds", "Telephone Ringing", "Clock ticking"], "Locked", "red-button", "none")
    create_lesson("Weekly quiz 2", ["Dog barking", "Cat meowing", "Cow mooing"], "Locked", "red-button", "none")

