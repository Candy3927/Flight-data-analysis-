import pandas as pd
import matplotlib.pyplot as plt


# read csv into a DataFrame
df = pd.read_csv("flight_data.csv")


# filter the DataFrame to only include records where arrival delay is between -60 and 120 mins
df = df[df["arr_delay"].between(-60, 120)]


# print summary statistics of the "arr_delay" column only
print(df["arr_delay"].describe())


# extract the "arr_delay" values as a numpy array (this excludes the column name)
sample = df.arr_delay.values


# get bin width of 5 mins
max_val = sample.max()
min_val = sample.min()
the_range = max_val - min_val
bin_width = 5
bin_count= int(the_range/bin_width)

# plot histogram of flight delay time distribution

plt.hist(sample, color='blue', edgecolor='black', bins=bin_count)
plt.title("Histogram of Arrival Delays")
plt.xlabel("Delay (min)")
plt.ylabel("Flights")
plt.show()