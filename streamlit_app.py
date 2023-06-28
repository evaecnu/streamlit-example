from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st



with st.form("daban",clear_on_submit=True):
   choice= st.selectbox('if the xpy in blacklist?',('yes','no'))
    st.write('youselect,choice')
    
