from datetime import datetime

dt = datetime(2024, 1, 1, 14, 30)
formatted = dt.strftime("%d %B %Y, %H:%M")
print(formatted)