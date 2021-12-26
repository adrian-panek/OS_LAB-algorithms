from collections import namedtuple
import csv

Process = namedtuple("Process", "arrival_time burst_time")
processes = []

with open("test_data.csv") as csvfile:
    filereader = csv.reader(csvfile, delimiter=",")
    for row in filereader:
        processes.append(Process(row[0], row[1]))

sorted_processes = sorted(processes, key=lambda x: x.arrival_time)

completion_time = []
for i in range(len(sorted_processes)):
    if (i==0):
        completion_time.append(int(sorted_processes[0][1]))
    else:
        completion_time.append(int(completion_time[i-1]) + int(sorted_processes[i][1]))

turn_around_time = []
for i in range(len(sorted_processes)):
    turn_around_time.append(int(completion_time[i]) - int(sorted_processes[i][1]))

waiting_time = []
for i in range(len(sorted_processes)):
    waiting_time.append(int(turn_around_time[i]) - int(sorted_processes[i][0]))


for i in range(len(sorted_processes)):
    print(f"CT: {completion_time[i]}")
    print(f"WT: {waiting_time[i]}")