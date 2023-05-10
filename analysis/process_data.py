import os
import datetime

debugLVL = 0 # set to 0 for no debug

class user_datapoint:
    def __init__(self, username, terminal, time, idle, pid, device):
        self.username = username
        self.terminal = terminal # like "pts/0" or "tty7"
        self.time = time # datetime object (not sure what it means tho)
        self.idle = idle # probably idle time?
        self.pid = pid
        self.device = device

    def __str__(self):
        return f"user={self.username}, term={self.terminal}, time={self.time}, idle={self.idle}, pid={self.pid}, device={self.device}"


class server_datapoint:
    def __init__(self, server, time, users):
        self.server = server
        self.time = time # datetime object
        self.users = users # list of user_datapoint type

    def __str__(self):
        userString = '\n\t'.join([str(x) for x in self.users])
        return f"{self.server} @ {self.time}\n\t{userString}"

def debug(message, level=1):
    if debugLVL >= level:
        print("[DEBUG]", message)


def get_datetime_object(date, time):
    # ex date="2023-05-09", time="13:07"
    isoString = f"{date}T{time}-05:00"
    datetimeObject = datetime.datetime.fromisoformat(isoString)
    return datetimeObject



def parse_user_line(line):
    data = line.split(" ")
    data = [x for x in data if x] # remove empty items
    
    # handle different types of data (with "-u" and without "-u")
    if len(data) == 5:
        # short option (without "who -u")
        username, terminal, date, time, device = data
        idle = None
        pid = None
    
    elif len(data) == 7:
        # long option (with "who -u")
        username, terminal, date, time, idle, pid, device = data
    
    else:
        raise ValueError(f"ERROR with user data line \"{line}\", has {len(data)} collumns, should be 5 or 7") # unsure if "ValueError" is right but oh well


    datetimeObj = get_datetime_object(date, time)
    return user_datapoint(username, terminal, time, idle, pid, device)



def get_logs(log_path="../logs"):
    data=[]

    # for each file (one per day)
    for filename in sorted(os.listdir(log_path)):
        filename = os.path.join(log_path,filename)
        debug(f'opening file "{filename}"')

        # open file
        with open(filename, "r") as f:
            for line in f:
                line = line.replace("\n", "") # strip newline
                debug(f'line is "{line}"', 2)

                # line like "server4 @ 2023-05-09 11:20:03"
                if line.startswith("server"): # detect start of server chunk
                    server, time = line.split(" @ ")
                    date, time = time.split(" ")
                    time = get_datetime_object(date, time)
                    data.append(server_datapoint(server, time, []))

                elif "{" in line:
                    continue

                elif  "}" in line:
                    # end of data chunk
                    debug("reached end of data chunk, data[-1] is:" + str(data[-1]), 2)
                    continue
                
                elif line == "":
                    continue

                # line contains user data
                else:
                    userDatapoint = parse_user_line(line)
                    data[-1].users.append(userDatapoint)
    
    return data
