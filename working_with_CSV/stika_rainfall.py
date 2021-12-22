import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls_amount = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        rainfall = float(row[3])
        dates.append(current_date)
        rainfalls_amount.append(rainfall)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, rainfalls_amount, c="green")
ax.set_title("Monthly rainfall amount in Stika", fontsize=22)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall amount", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()