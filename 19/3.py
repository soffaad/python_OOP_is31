import threading

def print_name(name):
    for _ in range(5):
        print(name)

threads = []
for i in range(3):
    t = threading.Thread(target=print_name, args=(f"Поток-{i+1}",))
    threads.append(t)
    t.start()
for t in threads:
    t.join()