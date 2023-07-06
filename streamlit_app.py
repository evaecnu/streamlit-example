import plotly.express as px
import pandas as pd
import streamlit as st

data = {
    'YUY': [2, 8, 4, 0, 1, 2, 0],
    'L': [24, 79, 18, 0, 1, 35, 6],
    'O': [80, 692, 60, 5, 4, 76, 26]
}

df = pd.DataFrame(data)
df.index = ['A 一个人住', 'B 与肉体家人合住', 'C 与外邦合住', 'D 与GF果子合住', 'E 与冬园物料合住', 'F 与st家人合住', 'G 其他']
st.dataframe(df)

cols = st.columns([1, 1])
with cols[0]:
    team_type = st.selectbox('球队', ['YUY', 'L', 'O'])

    fig = px.pie(df, values=team_type, names=['A一个人住', 'B与肉体家人合住', 'C与外邦合住', 'D与GF果子合住', 'E与冬园物料合住', 'F与st家人合住', 'G其他'],
                 title=f' {team_type} 队居住情况',
                 height=300, width=200)
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
    st.plotly_chart(fig, use_container_width=True)

with cols[1]:
   st.bar_chart(df)
