import pandas as pd
import csv
import plotly.express as px
import statistics as st
import random as r
import numpy as np

df = pd.read_csv("Project112_data.csv")
quant_saved = df["quant_saved"].tolist()
female = df["female"].tolist()
savings_data = list(df)

mean = st.mean(quant_saved)
print("The mean is " + str(mean))
median = st.median(quant_saved)
print("The median is " + str(median))
mode = st.mode(quant_saved)
print("The mode is " + str(mode))
st_dev = st.stdev(quant_saved)
print("The Standard deviation is " + str(st_dev))

def random_set(counter):
    subset = []
    for i in range(0, counter):
        random_index = r.randint(0, len(quant_saved)-1)
        value = quant_saved[random_index]
        subset.append(value)
    return subset

data_set = []

def calculate_mean(dataset, counter):
    data_set = random_set(counter)
    mean2 = st.mean(data_set)
    return mean2

def calculate_median(dataset, counter):
    data_set = random_set(counter)
    median2 = st.median(data_set)
    return median2

def calculate_mode(dataset, counter):
    data_set = random_set(counter)
    mode2 = st.mode(data_set)
    return mode2

mean2 = calculate_mean(quant_saved, 1000)
print("The mean2 of the sampling data is " + str(mean2))

median2 = calculate_median(quant_saved, 1000)
print("The median2 of the sampling data is " + str(median2))

mode2 = calculate_mode(quant_saved, 1000)
print("The mode2 of the sampling data is " + str(mode2))

quant_saved = []
wealthy = []
for data in savings_data:
    if data[5] != 0:
        quant_saved.append(data[5])
        wealthy.append(data[0])

correlation = np.corrcoef(quant_saved, wealthy)
print("The corelation between the quantity saved and of the person is wealthy or not is : " + str(correlation))