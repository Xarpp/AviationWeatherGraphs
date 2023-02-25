import requests
from bs4 import BeautifulSoup
import datetime
from plotly import offline


def get_data_from_URL(code, time_range):
    try:
        url = f"https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&" \
              f"requestType=retrieve&format=xml&stationString={code}&hoursBeforeNow={time_range}"
        url_data = requests.get(url).text
        soup = BeautifulSoup(url_data, features="xml")
        return soup
    except Exception as ex:
        # print(ex)
        return -1


def parse_data(soup):
    time_mass = []
    temp_mass = []
    if soup.find("errors").text == "" and int(soup.find("data").attrs["num_results"]) != 0:
        obs_time = soup.find_all("observation_time")
        temp_c = soup.find_all("temp_c")
        for time in reversed(obs_time):
            time_mass.append(datetime.datetime.strptime(time.text, '%Y-%m-%dT%H:%M:%SZ').strftime("%d.%m-%H:%M"))
        for temp in temp_c:
            temp_mass.append(temp.text)
        return time_mass, temp_mass
    else:
        # print("Invalid arguments in URL")
        return -2


def create_graph(data_time, data_temp):
    try:
        offline.plot({'data': [{'x': data_time, 'y': data_temp}],
                      'layout': {'title': 'Aviation weather',
                                 "xaxis": {"title": "Data", 'color': 'red'},
                                 "yaxis": {"title": "Temperature", 'color': 'red'},
                                 'font': dict(family='Comic Sans MS', size=10),
                                 'color': 'red'}},
                     auto_open=True, image='png', image_filename='plot_image',
                     output_type='file', image_width=1920, image_height=1080,
                     filename='Aviation_weather.html', validate=False)
    except Exception as ex:
        # print(ex)
        return -3


if __name__ == '__main__':
    pass
