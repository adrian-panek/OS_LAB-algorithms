from collections import namedtuple
import csv

Process = namedtuple("Process", "arrival_time burst_time")
processes = []

with open("test_data.csv") as csvfile:
    filereader = csv.reader(csvfile, delimiter=",")
    for row in filereader:
        processes.append(Process(row[0], row[1]))

sorted_processes = sorted(processes, key=lambda x: x.burst_time)

waiting_time = []
for i in range(len(sorted_processes)):
    if i==0:
        waiting_time.append(int(sorted_processes[-1][0]))
    else:
        waiting_time.append(int(sorted_processes[i][0]) + int(sorted_processes[i][1]))

turn_around_time = []
for i in range(len(sorted_processes)):
    turn_around_time.append(int(waiting_time[i-1]) + int(sorted_processes[i][1]))
    
print(sorted_processes)



    # print(f"Process: {i+1}")
    # print(f"WT: {waiting_time[i]}")
    # print(f"TAT: {turn_around_time[i]}")
    # print("-------------")

#[i][0] - arrival time
#[i][1] - burst time