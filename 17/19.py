import random
from datetime import date, timedelta

start = date(2024, 1, 1)
end = date(2024, 12, 31)
delta = end - start
random_days = random.randint(0, delta.days)
random_date = start + timedelta(days=random_days)
print(random_date)