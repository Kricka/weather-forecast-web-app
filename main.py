import streamlit as st
import plotly.express as px
from backend import get_data


# Add title, , place, days and kind of presentation
st.title("Weather Forecast for the Next Days")

place=st.text_input(label='Place')

days=st.slider(label="Forecast Days",min_value=1,max_value=5,step=1)

option=st.selectbox(label='Select data to view',options=['Temperature','Humidity','Sky'])

st.subheader(f"{option} for the next {days} days in {place}")


if place:


# Plot the chart

    try:
        # Get the temperature,humidity or sky data
        filtered_data = get_data(place, days)
        if option == "Temperature":
            dates=[item['dt_txt'] for item in filtered_data]
            temps=[item['main']['temp']/10 for item in filtered_data]
            figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": f"{option.title()}"})
            st.plotly_chart(figure)

        elif option=="Humidity":
            dates = [item['dt_txt'] for item in filtered_data]
            hum = [item['main']['humidity'] for item in filtered_data]
            figure = px.line(x=dates, y=hum, labels={"x": "Date", "y": f"{option.title()}"})
            st.plotly_chart(figure)

        elif option=="Sky":
            dates = [item['dt_txt'] for item in filtered_data]
            skies=[item['weather'][0]['main'] for item in filtered_data]
            images = {"Clouds": "images/clouds.png", "Clear": "images/clear.png", "Rain": 'images/rain.png',
                      "Snow": "images/snow.png"}
            img=[images[sky] for sky in skies]
            st.image(img,width=115,caption=skies)
    except KeyError:
        st.warning("This city doesn't exist", icon="⚠️")











