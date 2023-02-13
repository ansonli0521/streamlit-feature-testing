from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
import requests

if 'token' not in st.session_state:
    st.session_state.token = "Unauthenticated"

with st.form("login"):
    email = st.text_input("email:")
    password = st.text_input("password:", type="password")
    login = st.form_submit_button("login")
    if login:
        r = requests.post("http://u01-backoffice.fundpark.online:90/api/auth/login",
                          data={'email': email, 'password': password})
        st.write(r.json())
        if r.json().get("message") == "Unauthenticated":
            st.warning("Login Failed", icon="⚠️")
        else:
            st.success("Login Success")
            st.session_state.token = r.json().get("access_token")
            switch_page("streamlit_app")

st.markdown("http://0.0.0.0:8501/", unsafe_allow_html=True)
st.write(st.session_state.token)
