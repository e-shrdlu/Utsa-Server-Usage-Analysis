import process_data
import matplotlib.pyplot as plt
import datetime

log_path = "../logs"
data = process_data.get_logs(log_path)

s1_x_vals=[]
s1_y_vals=[]
s2_x_vals=[]
s2_y_vals=[]
s3_x_vals=[]
s3_y_vals=[]
s4_x_vals=[]
s4_y_vals=[]

for datapoint in data:

    # if datapoint.time < datetime.datetime.fromisoformat("2023-05-02T00:00:00-05:00"):
    #     continue
    # if datapoint.time.minute % 60 != 0 and datapoint.time.hour % 5 != 0:
    #     continue
    if datapoint.time.day != 5:
        continue
    if datapoint.server == "server1":
        s1_x_vals.append(datapoint.time)
        s1_y_vals.append(len(datapoint.users))
    elif datapoint.server == "server2":
        s2_x_vals.append(datapoint.time)
        s2_y_vals.append(len(datapoint.users))
    elif datapoint.server == "server3":
        s3_x_vals.append(datapoint.time)
        s3_y_vals.append(len(datapoint.users))
    elif datapoint.server == "server4":
        s4_x_vals.append(datapoint.time)
        s4_y_vals.append(len(datapoint.users))


l1 = plt.plot(s1_x_vals, s1_y_vals, "r-", label="fox1")
l2 = plt.plot(s2_x_vals, s2_y_vals, "y-", label="fox2")
l3 = plt.plot(s3_x_vals, s3_y_vals, "g-", label="fox3")
l4 = plt.plot(s4_x_vals, s4_y_vals, "b-", label="fox4")
plt.title("server usage over time")
plt.xlabel("time")
plt.ylabel("number of users")
plt.legend(loc="upper left")
plt.show()