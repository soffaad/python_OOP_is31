import threading

def print_numbers(name):
    for i in range(1, 6):
        print(f"{name}: {i}")

t1 = threading.Thread(target=print_numbers, args=("Поток A",))
t2 = threading.Thread(target=print_numbers, args=("Поток B",))
t1.start()
t2.start()
t1.join()
t2.join()