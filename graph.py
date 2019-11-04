import datetime
from matplotlib import pyplot as plt
from weather import get_weather
def graph(x, y):
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.xlim(0, 24, 2)
    plt.ylim(10, 60)
    plt.plot(x, y)
    plt.show()
    #plt.savefig("weather graph.pdf")