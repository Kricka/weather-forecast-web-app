import streamlit as st

st.title("Weather Forecast for the Next Days")


st.text_input(label='Place')


days=st.slider(label="Forecast Days",min_value=1,max_value=5,step=1)


option=st.selectbox(label='Select data to view',options=['Temperature','Humidity'])

st.header(f"{option} for the next {days} days in Tirana")