from queue import Queue 
import csv
  
def find_fault_data(data, n, frame_number):
    total_page_fault = 0
    set = []
    #symulacja kolejki
    queue = Queue() 
    #inicjalizacja zmiennej zliczającej strony
    page_fault_count = 0
    for i in range(n):
        # Sprawdzanie czy w tablicy zmieszczą się jeszcze dane
        if (len(set) < frame_number):
            # Umieszczanie danych w tablicy, jeśli jeszcze ich tam nie ma
            # co równocześnie już zwiększa nam licznik brakujących stron
            if (data[i] not in set):
                set.append(data[i]) 
                page_fault_count += 1
                #umieszczenie danych w kolejce
                queue.put(data[i])
        # Działanie zgodnie z zasadą FIFO, jeśli kolejka jest pełna
        # (usunięcie starej strony i umieszczenie nowej)
        else:
            # Sprawdzenie, czy w tablicy znajduje się już dana strona
            if (data[i] not in set):
                # Usunięcie pierwszej strony z kolejki
                val = queue.queue[0] 
                queue.get() 
                # Remove the indexes page 
                set.remove(val) 
                # umieszczenie aktualnej strony 
                set.append(data[i]) 
                # umieszczenie aktualnej strony 
                # w kolejce 
                queue.put(data[i]) 
                page_fault_count += 1
    return page_fault_count
  
if __name__ == '__main__':
    data = []
    output = ""
    frame_number = 5
    total_page_fault = 0
    #zmienna, która wczytuje każdy z plików po kolei
    for i in range(0,10):
        with open(f"../../data/page-replacement/page-replacement-data{i}.csv") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",")
            for item in filereader:
                data = item
                n = len(data)
                #wywołanie funkcji, która zlicza brakujące strony w iteracji
                total_page_fault += find_fault_data(data, n, frame_number)
                output += (f"Page faults were: {find_fault_data(data, n, frame_number)} \n")
                output += f"Page fault count: {total_page_fault} \n"
                file = open("../../output/page-replacement/fifo-output.txt", "w+")
                file.write(output)
                file.close()
                print()
    
    