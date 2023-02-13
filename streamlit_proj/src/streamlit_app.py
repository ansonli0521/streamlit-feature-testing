from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import date

dat = {
    "EN": "date",
    "CH": "日期"
}

lan = {
    "EN": "Language",
    "CH": "語言"
}

tit = {
    "EN": "Fundpark 2.0",
    "CH": "豐泊 2.0"
}

c = 0
option = []
option.append("EN")
temp = option[c]
d = [date.today()]

st.header("fundpark")

with st.sidebar:
    ph1 = st.empty()
    ph2 = st.empty()
    if option[c] == "EN":
        ndx = 0
    else:
        ndx = 1
    with ph1.container():
        option.append(ph1.selectbox(lan[option[c]], [
                      "EN", "CH"], index=ndx, key="ph1"+str(c)))
    with ph2.container():
        d.append(ph2.date_input(dat[option[c]], d[c], key="ph2"+str(c)))
    c += 1

    while option[c] != temp:
        temp = option[c]
        ph1.empty()
        ph2.empty()
        if option[c] == "EN":
            ndx = 0
        else:
            ndx = 1
        with ph1.container():
            option.append(ph1.selectbox(lan[option[c]], [
                          "EN", "CH"], index=ndx, key="ph1"+str(c)))
        with ph2.container():
            d.append(ph2.date_input(dat[option[c]], d[c], key="ph2"+str(c)))
        c += 1

st.title(tit[option[c]])
