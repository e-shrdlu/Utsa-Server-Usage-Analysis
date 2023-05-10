import process_data
import matplotlib.pyplot as plt
import datetime
import numpy as np

log_path = "../logs"
data = process_data.get_logs(log_path)

s1 = 0
s2 = 0
s3 = 0
s4 = 0

for datapoint in data:
    if datapoint.server == "server1":
        s1 += len(datapoint.users)
    elif datapoint.server == "server2":
        s2 += len(datapoint.users)
    elif datapoint.server == "server3":
        s3 += len(datapoint.users)
    elif datapoint.server == "server4":
        s4 += len(datapoint.users)

labels = ["fox1", "fox2", "fox3", "fox4"]
usage = [s1, s2, s3, s4]
plt.pie(usage, labels=labels, autopct='%1.1f%%', colors=['red','orange','green','blue'])
plt.title("server usage over time")
plt.show()