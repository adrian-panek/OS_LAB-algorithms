import random

def gen_random():
    return random.randint(0,10)

for i in range(0,100):
    for _ in range(0, 100):
        output = f"{gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random(), gen_random()}\n"
        file = open(f"../data/page-replacement/page-replacement-data{i}.csv", "a+")
        file.write(output)
        file.close()

