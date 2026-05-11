import threading
import queue
import time

def worker(q, name):
    while True:
        task = q.get()
        if task is None:
            break
        print(f"{name} обрабатывает задачу {task}")
        time.sleep(0.5)
        q.task_done()

q = queue.Queue()
workers = []
for i in range(3):
    t = threading.Thread(target=worker, args=(q, f"Worker-{i+1}"))
    t.start()
    workers.append(t)

for task in range(10):
    q.put(task)

for _ in workers:
    q.put(None)
for t in workers:
    t.join()