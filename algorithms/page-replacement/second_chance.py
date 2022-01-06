import numpy

#funkcja przyznająca drugą szansę stronie
def assign_second_chance(x, arr, second_chance, frame_number):
    for i in range(frame_number):
        #sprawdzenie, czy strona już jest w pamięci
        if arr[i] == x:
            #przyznanie stronie drugiej szansy
            second_chance[i] = True
            #zwracana wartość "True", gdy w pamięci dana strona już się znajduje
            return True
    #zwracana wartość "False", gdy w pamięci nie ma danej strony
    return False

#dodanie nowej strony do pamięci
def update_memory(x, arr, second_chance, frame_number, pointer):
    while True:
        #szukanie strony, która nie ma drugiej szansy
        if not second_chance[pointer]:
            #zastąpienie znalezionej strony nową
            arr[pointer] = x
            return (pointer + 1) % frame_number
        #zwracana wartość "False", jeśli okazuje się, że strona ma jeszcze jedną szanse
        second_chance[pointer] = False
        pointer = (pointer + 1) % frame_number

def find_fault_pages(data, frame_number):
    pointer = 0
    #licznik brakujących stron
    page_fault_count = 0
    arr = [0]*frame_number
    #lista wszystkich "drugich szans" w danym przykładzie
    second_chance = [False] * frame_number
    #ładowanie danych z pliku csv
    
    for i in range(len(data)):
        x = data[i]
        if not assign_second_chance(x, arr, second_chance, frame_number):
            pointer = update_memory(x, arr, second_chance, frame_number, pointer)
            page_fault_count+=1
    print(f"Total page faults were: {page_fault_count}")

data = []
with open("../../data/page-replacement/test_data.csv") as file:
    data = numpy.loadtxt(file, delimiter=",")
    
frame_number = 3

find_fault_pages(data, frame_number)