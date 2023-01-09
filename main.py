import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place=st.text_input(label='Place')

days=st.slider(label="Forecast Days",min_value=1,max_value=5,step=1)

option=st.selectbox(label='Select data to view',options=['Temperature','Humidity'])

st.subheader(f"{option} for the next {days} days in {place}")

a,b=get_data(place,option,days)
figure = px.line(x=a, y=b, labels={"x": "Date", "y": f"{option.title()}"})
st.plotly_chart(figure)





