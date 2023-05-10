import process_data
from process_data import server_datapoint, user_datapoint
import matplotlib.pyplot as plt
import datetime
import numpy as np


"""load logs"""
log_path = "../logs"
data = process_data.get_logs(log_path)

x_vals=[]
y_vals=[]


"""options"""
# timezone=datetime.timezone(datetime.timedelta(hours=-5)) # UTC-5
# cutoff_before = datetime.datetime(2023,5,3,2, tzinfo=timezone)
running_avg_window_size = int(15)


"""sum all datapoints within 5 minutes into one"""
newdata = []
while data:
    datapoint = data.pop()
    for i in range(len(data))[::-1]:
        # check if dates within 5 minutes of each other AND that not the same server
        # convert to seconds so we can use absolute value
        if abs((datapoint.time - data[i].time).total_seconds()) < datetime.timedelta(minutes=1).total_seconds():
            if data[i].server != datapoint.server:
                d = data.pop(i)
                datapoint.users += d.users
    datapoint.server = "combined"
    newdata.append(datapoint)

"""sort datapoints to be in chronological order"""
newdata.sort(key=lambda x: x.time.timestamp())


"""get x/y co-ordinates from data"""
for datapoint in newdata:
    # if datapoint.time <= cutoff_before: # remove outlier?
    #     continue
    x_vals.append(datapoint.time)
    y_vals.append(len(datapoint.users))


y_avg = []
"""get running average"""
for i in range(len(y_vals)):
    left = max(i-running_avg_window_size, 0) # left end of range
    right = min(i+running_avg_window_size, len(y_vals)) # right end of range
    window = y_vals[left:right] # range to get avg from
    y_avg.append(sum(window)/len(window)) # add average to list


plt.plot(x_vals, y_vals, "ro")
plt.plot(x_vals, y_avg, "b-")
plt.title(f"Server Usage Over Time")
plt.xlabel("Time")
plt.ylabel("Number of Active Logins")
plt.show()