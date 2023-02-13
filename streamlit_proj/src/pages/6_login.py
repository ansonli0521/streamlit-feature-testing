from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import requests

with st.form("login"):
    email = st.text_input("email:")
    password = st.text_input("password:", type="password")
    login = st.form_submit_button("login")
    if login:
        r = requests.post("http://u01-backoffice.fundpark.online:90/api/auth/login",
                          data={'email': email, 'password': password})
        st.write(r.text)
        if r.json().get("message") == "Unauthenticated":
            st.warning("Login Failed", icon="⚠️")
        else:
            st.success("Login Success")
