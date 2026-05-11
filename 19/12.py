import threading
import time
import random

def io_sim(name, delay):
    print(f"{name}: начало загрузки")
    time.sleep(delay)
    print(f"{name}: загрузка завершена за {delay:.2f} сек")

if __name__ == "__main__":
    threads = []
    for i in range(3):
        t = threading.Thread(target=io_sim, args=(f"Файл-{i+1}", random.uniform(0.5, 2)))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()