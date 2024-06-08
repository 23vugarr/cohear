import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()

st.write(
    """
#  Your Profile

This is a secret page that only logged-in users can see.

Super duper secret.

Shh....

"""
)