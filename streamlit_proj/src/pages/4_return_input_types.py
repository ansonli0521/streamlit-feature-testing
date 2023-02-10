from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import datetime
from datetime import date
from PIL import Image

with st.form("input type",True):
    text = st.text_input("text:")
    st.write("input text:", text)
    password = st.text_input("password:",type="password")
    st.write("input password:", password)
    radio = st.radio("radio", ("Yes","No"))
    st.write("radio option:", radio)
    checkbox = st.checkbox("checkbox")
    st.write("checkbox tick:", checkbox)
    submit = st.form_submit_button("submit")
    color = st.color_picker('color', '#00f900')
    st.write('color is:', color)
    dat = st.date_input("input date",date.today())
    st.write('date:', dat)
    t = st.time_input("input time",datetime.now())
    st.write('time:', t)
    im = Image.open(r"/Users/ansonli/Downloads/fp_logo.png")
    st.image(im, caption='image')
    int = st.number_input("input int",value=0)
    st.write("int:", int)
    float = st.number_input("input float",value=0.0)
    st.write("float:", float)
    range = st.slider("range:", -100, 100, step=1)
    st.write("num in range:", range)
    if submit:
        st.write("submitted and reset", submit)
button = st.button("button")
if button:
    st.write("clicked", button)