from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import date


def submit():
    st.session_state.form_disabled = True
    return


if 'form_disabled' not in st.session_state:
    st.session_state.form_disabled = False
with st.form("Proposed Financing Structure"):
    fin_struc = st.text_input(
        "Financing Structure :red[*]", disabled=st.session_state.form_disabled)
    limit = st.text_input(
        "Requested Limit (USD) :red[*]", disabled=st.session_state.form_disabled)
    tenor = st.text_input(
        "Requested Tenor (Days) :red[*]", disabled=st.session_state.form_disabled)
    st.write("**Payment Controlled by:**")
    cols = st.columns(2)
    with cols[0]:
        name = st.text_input(
            "Name of Payment Gateway :red[*]", disabled=st.session_state.form_disabled)
    with cols[1]:
        cus_id = st.text_input(
            "Customer ID in Payment Gateway :red[*]", disabled=st.session_state.form_disabled)
    control = st.radio(
        "Additional Payment Control from Affiliated Company :red[*]", ("Yes", "No"), disabled=st.session_state.form_disabled)
    if st.form_submit_button("Submit", on_click=submit, disabled=st.session_state.form_disabled):
        st.write("Submitted")
        form_data = [fin_struc, limit, tenor, name, cus_id, control]
        st.write("fin_struc: " + form_data[0])
        st.write("limit: " + form_data[1])
        st.write("tenor: " + form_data[2])
        st.write("name: " + form_data[3])
        st.write("cus_id: " + form_data[4])
        st.write("control: " + form_data[5])
