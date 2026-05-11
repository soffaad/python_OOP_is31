import multiprocessing

def cpu_bound(x):
    for _ in range(3):
        _ = sum(i*i for i in range(1000000))
    return f"Процесс {x} завершён"

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        results = pool.map(cpu_bound, range(4))
        for r in results:
            print(r)
    print("CPU-bound задача выполнена")