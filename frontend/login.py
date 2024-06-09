import streamlit as st
from time import sleep
from navigation import make_sidebar
from src.auth import AuthController
from src.schemas.user import UserRegister, UserLogin

make_sidebar()
backend_url = "http://localhost:9090"

auth_controller = AuthController(backend_url)

with st.container():
    register_tab, login_tab = st.tabs(['Register', 'Log in'])

    with register_tab:
        with st.form(key='register_form'):
            user = UserRegister(name="", surname="", phoneNumber=0, birthday="", password="")
            user.name = st.text_input("Name")
            user.surname = st.text_input("Surname")
            user.phoneNumber = st.text_input("Phone Number")
            user.password = st.text_input("Password", type="password")
            register_button = st.form_submit_button("Register")
            if register_button:
                # some additional testing skipping for now
                res = auth_controller.register(user)
                if res:
                    st.session_state.logged_in = True
                    st.session_state.phoneNumber = user.phoneNumber
                    st.success("Logged in successfully!")
                    sleep(0.5)
                    st.switch_page("pages/dashboard.py")
                else:
                    st.error("error while registering...")
                # register_user(phone_number, name, surname, password)
                # st.experimental_set_query_params(logged_in=True)

    with login_tab:
        with st.form(key='login'):
            user_login = UserLogin(password="", phoneNumber=0)

            user_login.phoneNumber = st.text_input('Phone number')
            user_login.password = st.text_input('Password', type="password")
            login_button = st.form_submit_button('Login')
            if login_button:
                res, jwt_response = auth_controller.login(user_login)
                if res:
                    st.session_state.logged_in = True
                    st.session_state.phoneNumber = int(user_login.phoneNumber)
                    st.session_state.jwt = jwt_response
                    st.success("Logged in successfully!")
                    sleep(0.5)
                    st.switch_page("pages/dashboard.py")
                else:
                    st.error("Incorrect username or password")
