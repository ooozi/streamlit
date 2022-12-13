import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader

def login():
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status :
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.title('Some content')
    elif authentication_status == False:
        st.error('Username/Password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter name and password')

    # reset password
    if authentication_status:
        try:
            if authenticator.reset_password(username, 'Reset Password'):
                st.success('Password Changed')
        except Exception as e:
            st.error(e)

    # user registration
    try:
        if authenticator.register_user("Register User", preauthorization=False):
            st.success("User registered successfully")
    except Exception as e:
        st.error(e)

    # forgot password
    try:
        username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot Password')
        if username_forgot_pw:
            st.success("New passowrd sent securely")
            st.write(username_forgot_pw, email_forgot_password, random_password)
        elif username_forgot_pw == False:
            st.error("Username not found")
    except Exception as e:
        st.error(e)

    # forgot username
    try:
        username_forgo_username, email_forgot_username = authenticator.forgot_username("Forgot Username")
        if username_forgo_username:
            st.success("Username sent securely")
        elif username_forgo_username == False:
            st.error("Email not found")
    except Exception as e:
        st.error(e)

    # update user details
    if authentication_status:
        try:
            if authenticator.update_user_details(username, "Update User details", "sidebar"):
                st.success("Entries updated successfully")
        except Exception as e:
            st.error(e)

    with open("./config.yaml", "w") as file:
        st.write(config)
        yaml.dump(config, file, default_flow_style=False)