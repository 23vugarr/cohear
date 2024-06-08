# import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
# from hashlib import sha256
# from streamlit_cookies_controller import CookieController

# controller = CookieController()

# # Load configuration from YAML file
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# # Create an authenticator object
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )


# def register_user(phone_number, name, surname, password):
#     if phone_number not in config['credentials']['phone_number'] :
#         config['credentials']['phone_number'][phone_number] = {'name': name, 'surname': surname, 'password': password}
#         with open('config.yaml', 'w') as file:
#             yaml.dump(config, file)
#         st.success("Registration susccessful! Please log in.")
#     else:
#         st.error("User already exists.")


# def login_user(phone_number, password):
#     ...
#     return True





# register_tab, login_tab = st.tabs(['Register', 'Log in'])
# with st.expander('Register', expanded=not st.session_state.get('authentication_status', False)):
#     with register_tab:
#         with st.form(key='register_form'):
#             phone_number = st.text_input("Phone Number")
#             name = st.text_input("Name")
#             surname = st.text_input("Surname")
#             password = st.text_input("Password", type="password")
#             register_button = st.form_submit_button("Register")
#             if register_button:
#                 register_user(phone_number, name, surname, password)
#     with login_tab:
#         with st.form(key='login'):
#             phone_number = st.text_input('Phone number')
#             password = st.text_input('Password')
#             login_button = st.form_submit_button('login')
#             if login_button:
#                 if login_user(phone_number, password):
#                     st.session_state['authentication_status'] = True
#                     st.rerun()
                

# if st.session_state.get("authentication_status"):
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state.get("authentication_status") == False:
#     st.error('Username/password is incorrect')
# elif st.session_state.get("authentication_status") == None:
#     st.warning('Please enter your username and password')
import streamlit as st
import yaml
from yaml.loader import SafeLoader
from hashlib import sha256

# Load configuration from YAML file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Define registration function
def register_user(phone_number, name, surname, password):
    if phone_number not in config['credentials']['phone_number']:
        config['credentials']['phone_number'][phone_number] = {'name': name, 'surname': surname, 'password': password}
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file)
        st.success("Registration successful! Please log in.")
    else:
        st.error("User already exists.")

# Define login function
def login_user(phone_number, password):
    # if phone_number in config['credentials']['phone_number'] and config['credentials']['phone_number'][phone_number]['password'] == password:
    #     return True
    # else:
    #     return False
    ...
    return True

# Define logout function
def logout_user():
    st.session_state['authentication_status'] = False
    st.session_state['logout_clicked'] = True

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
                register_user(phone_number, name, surname, password)
                st.experimental_set_query_params(logged_in=True)

    with login_tab:
        with st.form(key='login'):
            phone_number = st.text_input('Phone number')
            password = st.text_input('Password', type="password")
            login_button = st.form_submit_button('Login')
            if login_button:
                if login_user(phone_number, password):
                    st.session_state['authentication_status'] = True
                    st.experimental_set_query_params(logged_in=True)
                    st.success(f'Welcome Gultaj!')

if st.session_state.get("authentication_status"):
    logout_button = st.button('Logout')
    if logout_button:
        logout_user()
        st.success('Logged out successfully!')
    if st.session_state.get('logout_clicked') :
        st.experimental_set_query_params(logged_in=False)

if st.session_state.get("authentication_status"):
    st.title('Some content')

if st.experimental_get_query_params().get('logged_in'):
    st.write('You are logged in! Redirecting to another page...')
    # Redirect the user to another page using st.experimental_set_query_params
    st.experimental_set_query_params()