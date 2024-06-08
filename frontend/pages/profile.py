import streamlit as st
from time import sleep
from navigation import make_sidebar
from src.profile import ProfileController
from login import backend_url

make_sidebar()

profileController = ProfileController(backend_url=backend_url)
pc = profileController.get_profile_info(st.session_state.get("phoneNumber"))
a = 2
st.write(
    f"""
#  Your Profile 🤠
### Name {pc.name}
### Account created {pc.createdAt}
### Streaks {pc.streaks}🔥
### Longest streaks 4 🔥
### Badges:
"""
)
st.image(['images/good_listener.png', 'images/good_streaker.png', 'images/lazy_learner.png'], width=200, caption=['Good Listener', 'Streaks maker', 'Lazy learner'])

# * optional kwarg unsafe_allow_html = True