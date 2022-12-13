import os
import streamlit as st
from authentication import auth_main
from tutorial import dash
from dotenv import load_dotenv

def main():
    load_dotenv(".env")
    st_sample = os.getenv("st_sample")
    auth_type = os.getenv("auth_type")

    print(st_sample)
    if st_sample == "auth":
        auth_main.login(auth_type)  
    elif st_sample == "dash":
        dash.main()

if __name__ == "__main__":
    main()