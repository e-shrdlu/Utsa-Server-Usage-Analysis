import process_data
from process_data import server_datapoint, user_datapoint
import matplotlib.pyplot as plt
import datetime

log_path = "../logs"
data = process_data.get_logs(log_path)

x_vals=[]
y_vals=[]

timezone=datetime.timezone(datetime.timedelta(hours=-5))

"""options"""
cutoff_before = datetime.datetime(2023,5,3,2, tzinfo=timezone)


# sum all datapoints within 5 minutes into one
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

for datapoint in newdata:
    if datapoint.time <= cutoff_before: # remove outlier?
        continue
    x_vals.append(datapoint.time)
    y_vals.append(len(datapoint.users))


l = plt.plot(x_vals, y_vals, "r-")
plt.title("server usage over time")
plt.xlabel("time")
plt.ylabel("number of active logins")
plt.show()