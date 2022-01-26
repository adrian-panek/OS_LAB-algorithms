import csv
from dataclasses import dataclass

@dataclass
class SJF:
    id: int
    arrival_time: int
    burst_time: int
    start_time: int = 0
    completion_time: int = 0
    turnaround_time: int = 0
    waiting_time: int = 0
    response_time: int = 0
    is_completed: bool = False

processes = []
for i in range(0,100):
    with open(f"../../data/cpu-scheduling/cpu-schedule-data{i}.csv") as csvfile:
        filereader = csv.reader(csvfile, delimiter=",")
        for row in filereader:
            processes.append(SJF(i,int(row[0]), int(row[1])))


n = len(processes)
prev = 0
completed: int = 0
current_time: int = 0
total_waiting_time: int = 0
total_turnaround_time: int = 0

while (completed != n):
    index: int = None
    mn: int = 999
    for i in range(n):
        if processes[i].arrival_time <= current_time and not processes[i].is_completed:
            if processes[i].burst_time < mn:
                mn = processes[i].burst_time
                index = i
            
            if processes[i].burst_time == mn:
                if processes[i].arrival_time < processes[index].arrival_time:
                    mn = processes[i].burst_time
                    index = i

    if index != None:
        processes[index].start_time = current_time
        processes[index].completion_time = processes[index].start_time + int(processes[index].burst_time)
        processes[index].turnaround_time = processes[index].completion_time - int(processes[index].arrival_time)
        processes[index].waiting_time = processes[index].turnaround_time - int(processes[index].burst_time)
        processes[index].response_time = processes[index].start_time - int(processes[index].arrival_time)
        processes[index].is_completed = True

        total_waiting_time += processes[index].waiting_time
        total_turnaround_time += processes[index].turnaround_time
        
        completed+=1
        current_time = processes[index].completion_time
        prev = current_time
    else:
        current_time+=1

output = ""
for i in range(n):
    output += ("--------------- \n")
    output += (f"Process {i+1}, CT: {processes[i].completion_time}, TAT: {processes[i].turnaround_time}, WT: {processes[i].waiting_time} \n")

avg_turnaround_time = total_turnaround_time / n
avg_waiting_time = total_waiting_time / n

file = open("../../output/cpu-scheduling/sjf-output.txt", "w+")
file.write(output)
file.write(f"AVG TAT: {avg_turnaround_time} \n")
file.write(f"AVG WT: {avg_waiting_time}")
file.close()