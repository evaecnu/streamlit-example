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
