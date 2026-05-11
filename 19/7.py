import threading
import queue

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Обработано: {item}")
        q.task_done()

q = queue.Queue()
t = threading.Thread(target=worker, args=(q,))
t.start()

for i in range(5):
    q.put(i)
q.put(None)
t.join()