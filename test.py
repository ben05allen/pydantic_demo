import pydantic
from schedules import Sale
import time

NUM_RUNS = 100_000

print(pydantic.__version__)

rows = [
    {
        "Date": "2023-3-14",
        "Customer Name": "Nakamura",
        "Size (kg)": 2.5,
        "Amount": 2,
        "Unit Price": 450,
    },
    {
        "Date": "13/6/2023",
        "Customer Name": "Tanaka",
        "Size (kg)": "5kg",
        "Amount": 1,
        "Unit Price": 850,
    },
    {
        "Date": "12/09/23",
        "Customer Name": "Yamamoto",
        "Size (kg)": "20kg",
        "Amount": 4,
        "Unit Price": 3900,
    },
    {
        "Date": "15-12-2024",
        "Customer Name": "Suzuki",
        "Size (kg)": 20,
        "Amount": 2,
        "Unit Price": 4200,
    },
    {
        "Date": "15-Feb-2024",
        "Customer Name": "Kobayashi",
        "Size (kg)": 5,
        "Amount": 3,
        "Unit Price": 1975,
    },
]

start_time = time.time()
for _ in range(NUM_RUNS):
    for row in rows:
        Sale(**row)
print(time.time() - start_time)
