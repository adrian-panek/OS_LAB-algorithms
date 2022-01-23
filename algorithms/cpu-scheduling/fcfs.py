from collections import namedtuple
import csv

Process = namedtuple("Process", "arrival_time burst_time")
processes = []
total_waiting_time = 0
total_turnaround_time = 0

for i in range(0,100):
    with open(f"../../data/cpu-scheduling/cpu-schedule-data{i}.csv") as csvfile:
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
    total_turnaround_time += turn_around_time[i]

waiting_time = []
for i in range(len(sorted_processes)):
    waiting_time.append(int(turn_around_time[i]) - int(sorted_processes[i][0]))
    total_waiting_time += waiting_time[i]

output = ""

for i in range(len(sorted_processes)):
    output += ("--------------- \n")
    output += (f"Process {i+1}, CT: {completion_time[i]},  WT: {waiting_time[i]}, TAT: {turn_around_time[i]} \n")

avg_turnaround_time = total_turnaround_time / len(sorted_processes)
avg_waiting_time = total_waiting_time / len(sorted_processes)

file = open("../../output/cpu-scheduling/fcfs-output.txt", "w+")
file.write(output)
file.write(f"AVG TAT: {avg_turnaround_time} \n")
file.write(f"AVG WT: {avg_waiting_time}")
file.close()