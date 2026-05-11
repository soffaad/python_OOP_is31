def task1():
    for i in range(3):
        print(f"task1: строка {i}")

def task2():
    for i in range(3):
        print(f"task2: строка {i}")

print("Последовательное выполнение:")
task1()
task2()

print("\nПараллельное выполнение (потоки):")
import threading
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()