import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()



with st.container():
    register_tab, login_tab = st.tabs(['Register', 'Log in'])

    with register_tab:
        with st.form(key='register_form'):
            phone_number = st.text_input("Phone Number")
            name = st.text_input("Name")
            surname = st.text_input("Surname")
            password = st.text_input("Password", type="password")
            register_button = st.form_submit_button("Register")
            if register_button:
        # some additional testing skipping for now
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
                sleep(0.5)
                st.switch_page("pages/dashboard.py")
                # register_user(phone_number, name, surname, password)
                # st.experimental_set_query_params(logged_in=True)

    with login_tab:
        with st.form(key='login'):
            phone_number = st.text_input('Phone number')
            password = st.text_input('Password', type="password")
            login_button = st.form_submit_button('Login')
            if login_button:
                if phone_number == "0513423101" and password == "a":
                    st.session_state.logged_in = True
                    st.success("Logged in successfully!")
                    sleep(0.5)
                    st.switch_page("pages/dashboard.py")
                else:
                    st.error("Incorrect username or password")
