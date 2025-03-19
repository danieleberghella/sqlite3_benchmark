import csv
import random
import time

CSV_FILE = "data.csv"
NUM_RECORDS = 10000


def generate_csv(file_name, num_records):
    start_time = time.time()
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "age", "salary"])

        for i in range(1, num_records + 1):
            name = f"User{i}"
            age = random.randint(18, 65)
            salary = round(random.uniform(30000, 120000), 2)
            writer.writerow([i, name, age, salary])

    print(f"CSV generated in {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    print("Generating CSV file...")
    generate_csv(CSV_FILE, NUM_RECORDS)
