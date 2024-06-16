import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests


# function to get weather image
def get_weather_image(weather):
    for image, conditions in weather_images.items():
        if weather in conditions:
            return f"icons/{image}.png"
    return None


# function to get weather data
def get_weather_data(location):
    url = f"https://www.google.com/search?q={location.replace(' ', '')}+weather"
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    html = session.get(url)
    soup = bs(html.text, "html.parser")

    # get data points
    temp = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    area = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    time_and_sky = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    time = time_and_sky.split("\n")[0]
    weather = time_and_sky.split("\n")[1]

    return temp, time, area, weather


sg.theme("reddit")

# constants
weather_images = {
    "sun": ["Clear", "Sunny"],
    "part sun": [
        "Partly Sunny",
        "Mostly Sunny",
        "Partly Cloudy",
        "Mostly Cloudy",
        "Cloudy",
        "Overcast",
    ],
    "rain": [
        "Showers",
        "Scattered Showers",
        "Rain and Snow",
        "Light Rain",
        "Chance of Rain",
        "Rain",
    ],
    "thunder": [
        "Scattered Thunderstorms",
        "Chance of Storm",
        "Storm",
        "Thunderstorm",
        "Chance of TStorm",
    ],
    "fog": ["Mist", "Dust", "Fog", "Smoke", "Haze", "Flurries"],
    "snow": [
        "Freezing Drizzle",
        "Chance of Snow",
        "Sleet",
        "Snow",
        "Icy",
        "Light Snow",
        "Snow Showers",
        "Hail",
    ],
}

# layouts
image_col = sg.Column(
    [[sg.Image(filename="", key="-IMAGE-", background_color="white")]]
)
weather_col = sg.Column(
    [
        [
            sg.Text(
                "",
                key="-TEMP-",
                font="Calibri 25",
                background_color="red",
                text_color="white",
                pad=0,
                visible=False,
            )
        ],
        [
            sg.Text(
                "",
                key="-TIME-",
                font="Calibri 16",
                background_color="black",
                text_color="white",
                pad=0,
                visible=False,
            )
        ],
        [
            sg.Text(
                "",
                key="-LOCATION-",
                font="Calibri 16",
                background_color="white",
                text_color="black",
                pad=(0, 10),
                justification="center",
                visible=False,
            )
        ],
    ]
)

layout = [
    [
        sg.Input(key="-INPUT-", expand_x=True),
        sg.Button("Search", button_color="black", border_width=0, key="-SEARCH-"),
    ],
    [image_col, weather_col],
]

window = sg.Window("Weather App", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-SEARCH-":
        temp, time, area, weather = get_weather_data(values["-INPUT-"])
        weather_image = get_weather_image(weather)

        window["-LOCATION-"].update(f"📍: {area}", visible=True)
        window["-TIME-"].update(f"Time: {time}", visible=True)
        window["-TEMP-"].update(f"{temp}, {weather}", visible=True)
        window["-IMAGE-"].update(weather_image)
        window["-INPUT-"].update("")

window.close()
