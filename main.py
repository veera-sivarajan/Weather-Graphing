import csv
from get_time import get_time
from weather import get_weather
from graph import graph

if __name__ == "__main__":
    time = get_time()
    time_list = []
    with open('time_data.csv', 'a', newline= '') as time_file:
        time_file_write = csv.writer(time_file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        time_file_write.writerow([time])
    with open('time_data.csv', 'r') as time_data:
            read = csv.reader(time_data)
            for i in read:
                time_list.append(int(i[0]))
    
    weather = get_weather()
    weather_list = []
    with open('weather_data.csv', 'a', newline= '') as weather_file:
        weather_file_write = csv.writer(weather_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        weather_file_write.writerow([weather])
    with open('weather_data.csv', 'r') as weather_data:
        read = csv.reader(weather_data)
        for i in read:
            weather_list.append(float(i[0]))
    graph(time_list, weather_list)

    