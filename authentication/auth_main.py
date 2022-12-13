import os
from authentication import auth_yaml, auth_db

def login(auth_type="yaml"):
    """streamlit authentication sample

    Args:
        auth_type (str, optional): authentication type. Defaults to "yaml".
    """
    if auth_type == "yaml":
        auth_yaml.login()
    elif auth_type == "db":
        auth_db.login()

if __name__ == "__main__":
    login()