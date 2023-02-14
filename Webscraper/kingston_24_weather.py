import requests
from bs4 import BeautifulSoup


# webscraper that scrapes the last 24 hours of weather in kingston from
# https://weather.gc.ca/past_conditions/index_e.html?station=ygk
def kingston_24_hour_weather():
    url = "https://weather.gc.ca/past_conditions/index_e.html?station=ygk"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    # print(html.text) # prints the html of the website

    results = soup.find("tbody")
    # print(results) # prints the html of the table

    # temps stored in header3m, times stored in header1
    weather = results.find_all(headers="header3m")
    time = results.find_all(headers="header1")

    # print(weather[0].text.split("(")[1].split(")")[0])
    for i in range(len(time)):
        print(time[i].text + "--> " + weather[i].text.split("(")[1].split(")")[0] + " C")


kingston_24_hour_weather()
