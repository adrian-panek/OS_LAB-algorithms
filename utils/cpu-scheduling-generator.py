import random

num1 = 0
num2 = 0

for i in range(0,100):
    for _ in range(0, 100):
        for _ in range(1,2):
            num1 = random.randint(0,10)
            num2 = random.randint(0,10)
            output = f"{num1},{num2} \n"
            file = open(f"../data/cpu-scheduling/cpu-schedule-data{i}.csv", "a+")
            file.write(output)
            file.close()