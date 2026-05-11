import threading
import time

def daemon_task():
    for _ in range(10):
        print("Демон работает...")
        time.sleep(1)

if __name__ == "__main__":
    d = threading.Thread(target=daemon_task, daemon=True)
    d.start()
    time.sleep(3)
    print("Основная программа завершается, демон будет остановлен")