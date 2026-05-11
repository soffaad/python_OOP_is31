import multiprocessing

def sum_range(n):
    return sum(range(1, n+1))

if __name__ == "__main__":
    with multiprocessing.Pool(2) as pool:
        results = pool.map(sum_range, [100000, 100000])
    print(f"Суммы: {results}")