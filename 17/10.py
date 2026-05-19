from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=7)
print(future.date())