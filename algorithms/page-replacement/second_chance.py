#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import csv

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
    for i in range(len(data)):
        x = data[i]
        if not assign_second_chance(x, arr, second_chance, frame_number):
            pointer = update_memory(x, arr, second_chance, frame_number, pointer)
            page_fault_count+=1
    print(f"Total page faults were: {page_fault_count}")
    data = []


if __name__ == "__main__":
    frame_number = 5
    data = []
    for i in range(0,2):
        with open(f"../../data/page-replacement/test_data{i}.csv") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",")
            for item in filereader:
                data = item
                find_fault_pages(data, frame_number)
                    