import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
df_list = df['math score'].tolist()

mean = statistics.mean(df_list)
mode = statistics.mode(df_list)
median = statistics.median(df_list)
standard_deviation = statistics.stdev(df_list)

print('The mean is' , mean)
print('The mode is', mode)
print('The median is', median)
print('The standard deviation is', standard_deviation)

first_std_start , first_std_end = mean - standard_deviation , mean + standard_deviation
second_std_start , second_std_end = mean - 2*standard_deviation , mean + 2*standard_deviation
third_std_start , third_std_end = mean - 3*standard_deviation , mean + 3*standard_deviation

first_std_list = []

for result in df_list:
    if first_std_start < result < first_std_end:
        first_std_list.append(result)

first_percentage = len(first_std_list) * 100 / len(df_list) 
print('The percentage of data that lies between the first standard deviation is', first_percentage)

second_std_list = []

for result in df_list:
    if second_std_start < result < second_std_end:
        second_std_list.append(result)

second_percentage = len(second_std_list) * 100 / len(df_list) 
print('The percentage of data that lies between the second standard deviation is', second_percentage)

third_std_list = []

for result in df_list:
    if third_std_start < result < third_std_end:
        third_std_list.append(result)

third_percentage = len(third_std_list) * 100 / len(df_list) 
print('The percentage of data that lies between the third standard deviation is', third_percentage)