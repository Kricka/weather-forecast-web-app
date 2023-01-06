import streamlit as st
import plotly.express as px
import requests

st.title("Weather Forecast for the Next Days")


st.text_input(label='Place')


days=st.slider(label="Forecast Days",min_value=1,max_value=5,step=1)


option=st.selectbox(label='Select data to view',options=['Temperature','Humidity'])

st.subheader(f"{option} for the next {days} days in Tirana")



def get_data(days):
    dates=["2022-25-10","2022-26-10","2022-27-10",]
    temperatures=[10,11,12]
    temperatures=[days*i for i in temperatures]
    return dates,temperatures

d,t=get_data(days)

figure=px.line(x=d,y=t,labels={"x":"Date","y":"Temperature in (C)"})
st.plotly_chart(figure)
