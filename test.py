from schedules import Sale

NUM_RUNS = 100_000

row = {
    "Date": "2023-3-14",
    "Customer Name": "Nakamura",
    "Size (kg)": 2.5,
    "Amount": 2,
    "Unit Price": 450
}
for _ in range(NUM_RUNS):
    Sale(**row)