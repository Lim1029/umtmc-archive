from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import re

st.set_page_config(page_title="Technical Reports", page_icon="📹")
st.markdown("# Technical Reports")
st.sidebar.header("Technical Reports")
