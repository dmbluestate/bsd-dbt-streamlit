import streamlit as st
from PIL import Image

from src.pages.dbt_dashboard import render_page as render_page_dbt_dashboard
from src.shared.environment import Auth


def set_up_app():
    # Set a title and add a sidebar title
    st.title("DBT Dashboard")

    # add an image to the sidebar
    image = Image.open("./images/logo.png")
    st.sidebar.image(image, use_column_width=True)

    st.sidebar.title("Login")


def set_up_auth():

    input_user = st.sidebar.text_input("Username")
    input_pass = st.sidebar.text_input("Password", type="password")

    if not input_user or not input_pass:
        st.warning("Please input your user / pass.")
        st.stop()
    auth = Auth(user=input_user, password=input_pass)

    if not auth.is_auth():
        st.warning("Please, introduce the correct user/pass.")
        st.stop()

    return auth


def main():
    st.set_page_config(layout="wide")
    set_up_app()
    # set_up_auth()
    render_page_dbt_dashboard()


if __name__ == "__main__":
    main()
