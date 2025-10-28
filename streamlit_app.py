# streamlit,py
import streamlit as st
import requests
from dotenv import load_dotenv
import os
from recommender import recommend_outfit

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# --- Streamlit App ---
st.set_page_config(page_title="Smart Outfit Recommender", page_icon="👗", layout="centered")

st.title("👗 Smart Outfit Recommender")
st.write("Get weather updates and personalized outfit suggestions!")

city = st.text_input("Enter your city:", "Pune")

if st.button("Check Weather"):
    data = get_weather(city)

    if data.get("cod") != 200:
        st.error("City not found or invalid API key. Please check again.")
    else:
        st.subheader(f"🌦️ Weather in {city}")
        st.write(f"**Temperature:** {data['main']['temp']}°C")
        st.write(f"**Condition:** {data['weather'][0]['description'].title()}")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")

        # Get outfit recommendation
        recommendation = recommend_outfit(data)
        st.subheader("🧥 Outfit Recommendation")
        st.success(f"👕 {recommendation['outfit']}")
        st.info(f"💡 {recommendation['tip']}")
