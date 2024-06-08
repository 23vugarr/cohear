import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()
a = 2
st.write(
    """
#  Your Profile 🤠
### Name {user_name, user_surname}
### Account created {create_date}
### Streaks {current_streak}🔥
### Longest streaks {longest_streak} 🔥
### Badges:
"""
)
st.image(['images/good_listener.png', 'images/good_streaker.png', 'images/lazy_learner.png'], width=200, caption=['Good Listener', 'Streaks maker', 'Lazy learner'])

# * optional kwarg unsafe_allow_html = True