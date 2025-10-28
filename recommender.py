# recommender.py

def recommend_outfit(weather_data):
    """
    Recommend outfit based on weather conditions.
    """

    temp = weather_data["main"]["temp"]
    weather_condition = weather_data["weather"][0]["main"].lower()

    if temp < 15:
        outfit = "Warm jacket, sweater, jeans, and boots"
        tip = "It’s quite cold! Don’t forget gloves or a scarf."
    elif 15 <= temp < 25:
        outfit = "Full-sleeve shirt or light jacket with jeans"
        tip = "Mild weather — comfortable for outdoor activities."
    elif temp >= 25:
        outfit = "T-shirt, shorts, sunglasses, and light shoes"
        tip = "Stay hydrated and wear sunscreen."

    if "rain" in weather_condition:
        outfit += ", and carry an umbrella or raincoat"
        tip = "It's raining, stay dry!"

    elif "cloud" in weather_condition:
        outfit += ", maybe take a light jacket"
        tip = "Cloudy skies — weather might change."

    return {"outfit": outfit, "tip": tip}
