from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit.components.v1 import html

# Define your javascript
my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

# Execute your app
st.title("Javascript example")
html(my_html)


def next():
    st.session_state.notinum += 1
    return


noti = ["noti1", "noti2", "noti3"]
if 'notinum' not in st.session_state:
    st.session_state.notinum = 0
if 'next_disabled' not in st.session_state:
    st.session_state.next_disabled = False
if (len(noti) - st.session_state.notinum > 0):
    st.info('You have unread notification(s)', icon="🚨")
    expand_str = "notification (" + str(len(noti) -
                                        st.session_state.notinum) + ")"
    expand_status = True
else:
    expand_str = "notification"
    st.session_state.next_disabled = True
    expand_status = False
with st.expander(expand_str, expand_status):
    if st.session_state.notinum < len(noti):
        st.write(noti[st.session_state.notinum])
    else:
        st.write("no unread noti")
    st.button("Next", on_click=next, disabled=st.session_state.next_disabled)
