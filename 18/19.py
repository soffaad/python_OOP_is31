class MyContext:
    def __enter__(self):
        print("Start")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End")

with MyContext():
    print("Working...")