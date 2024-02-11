import pydantic
from schedules import Sale
import time   

NUM_RUNS = 100_000

print(pydantic.__version__)

row = {
    "Date": "2023-3-14",
    "Customer Name": "Nakamura",
    "Size (kg)": 2.5,
    "Amount": 2,
    "Unit Price": 450
}

start_time = time.time()
for _ in range(NUM_RUNS):
    Sale(**row)
print(time.time()-start_time)