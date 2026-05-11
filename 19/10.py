import threading
import multiprocessing
import time

def heavy_calc():
    return sum(i*i for i in range(500000))

if __name__ == "__main__":
    start = time.time()
    t1 = threading.Thread(target=heavy_calc)
    t2 = threading.Thread(target=heavy_calc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    thread_time = time.time() - start

    start = time.time()
    p1 = multiprocessing.Process(target=heavy_calc)
    p2 = multiprocessing.Process(target=heavy_calc)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    process_time = time.time() - start

    print(f"Потоки: {thread_time:.2f} сек")
    print(f"Процессы: {process_time:.2f} сек")