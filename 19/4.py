import threading
import time

def delayed_print(name, delay):
    for i in range(3):
        print(f"{name}: {i}")
        time.sleep(delay)

t1 = threading.Thread(target=delayed_print, args=("Без задержки", 0))
t2 = threading.Thread(target=delayed_print, args=("С задержкой 1с", 1))
t1.start()
t2.start()
t1.join()
t2.join()