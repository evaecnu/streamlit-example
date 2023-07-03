from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

"""
data = {'group':['v', 'b', 'o','b','v','o','b','v','b',0o','v', 'b', 'o','b','v','o','b','v','b','o','v', 'b', 'o','b','v','o','b','v','b','o','v', 'b', 'o','b','v','o','b','v','b','o','b', 'o','b','v','o','b','v','b','o'],
        'Live':['A','A','C','B','A','C','B','A','B','A','A','C','B','A','C','B','A','B','A','B','C','B','A','C','B','A','B','A','A','C','A','C','B','A','B','A','B','C','B','A','C','B','A','B','A','A','C','B','A','C'] }
df= pd.DataFrame(data)
print(df)
st.dataframe(df)

with st.form("daban",clear_on_submit=True):
   choice= st.selectbox('if the xpy in blacklist?',('yes','no'))
   xueli= st.selectbox('xpy degree?',('primary school','middle school'))
   job=st.text_input('xpy job')
   result=st.json({'choice':choice,'xueli':xueli,'job':job})
   submitted=st.form_submit_button("submit")
   

    
