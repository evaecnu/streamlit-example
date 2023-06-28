from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st



with st.form("daban",clear_on_submit=True):
   choice= st.selectbox('if the xpy in blacklist?',('yes','no'))
   xueli= st.selectbox('xpy degree?',('primary school','middle school'))
   job=st.text_input('xpy job')
   st.write('youselect,choice')
   submitted=st.form_submit_button('submit')
    
