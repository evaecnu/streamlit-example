import plotly.express as px
import pandas as pd
import streamlit as st

data = {
    'YUY': [2, 8, 4, 0, 1, 2, 0],
    'L': [24, 79, 18, 0, 1, 35, 6],
    'O': [80, 692, 60, 5, 4, 76, 26],
    'V': [142, 93, 74, 0, 4, 75, 15],
    'DY': [74, 111, 23, 1, 1, 99, 13],
    'HGY': [6, 24, 2, 0, 0, 3, 0],
    'LYH': [11, 48, 3, 1, 2, 5 ,5],
    'NN': [38, 77, 17, 0, 0, 23, 13],
    'YY': [50, 82, 6, 2, 1, 14, 7]
}

df = pd.DataFrame(data)
df.index = ['A Live Alone', 'B 与RTJR合Z', 'C 与WB合Z', 'D 与GFGG合Z', 'E 与DYWL合Z', 'F 与STJR合Z', 'G other']
st.dataframe(df)
st.divider()
#Chart 1:
st.subheader('各单位居住状况饼图')
team_type = st.selectbox('Please select the team to show:', ['YUY', 'L', 'O', 'V', 'DY', 'HGY', 'LYH', 'NN', 'YY'])

fig = px.pie(df, values=team_type, names=['A Live Alone', 'B 与RTJR合Z', 'C 与WB合Z', 'D 与GFGG合Z', 'E 与DYWL合Z', 'F 与STJR合Z', 'G other'],
            title=f' {team_type} 队居住情况',
            height=300, width=200)
fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
st.plotly_chart(fig, use_container_width=True)

#Chart 2:
st.divider()
st.subheader('各个单位在每个选项上的柱状对比图')
st.bar_chart(df)
