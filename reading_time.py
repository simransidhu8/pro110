import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("The population mean is", population_mean)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("The mean of the sampling data is", mean)
    fig = ff.create_distplot([df], ["reading time"], show_hist=False)

def setup():
    mean_list= []
    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()