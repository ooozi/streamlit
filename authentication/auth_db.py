import streamlit as st
import streamlit_authenticator as stauth
import authentication.database as db
from pathlib import Path
import pickle

def login():
    st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

    placeholder = st.empty()
    placeholder.info("Credentials")

    users = db.fetch_all_users()

    usernames = [user["key"] for user in users]
    names = [user["name"] for user in users]
    passwords = [user["password"] for user in users]

    credentials = { "usernames": {}}

    for username, name, password in zip(usernames, names, passwords):
        user_dict = {"name": name, "password": password}
        credentials["usernames"].update({username: user_dict})

    authenticator = stauth.Authenticate(credentials, 
        "sales_dashboard", "abcdef", cookie_expiry_days=30)

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status == False:
        st.error("Username/password is correct")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        placeholder.empty()

        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")
        st.sidebar.header("Please Filter Here:")
        