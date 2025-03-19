# SQLite3 Performance Benchmark

## This repository contains two Python scripts designed to benchmark SQLite3 database performance using different PRAGMA settings. The benchmark consists of two steps:

### CSV Generation
A script (`create_salary_CSV.py`) generates a CSV file (`data.csv`) containing randomly generated employee data, including ID, name, age, and salary.

### Database Import
A script (`save_data_from_CSV_to_database.py`) imports the CSV data into an SQLite database (`database.db`). The import process runs twice:
- **Without PRAGMA optimizations** (default settings)
- **With optimized PRAGMA settings** (adjusting `synchronous`, `journal_mode`, and `cache_size` for better performance)

Each script outputs the execution time in seconds to measure the performance difference.

---

## Installation & Usage

### Prerequisites
- Python 3.x

### Running the Benchmark

#### Generate the CSV file:
```bash
python create_salary_CSV.py
```

#### Run the database import benchmark:
```bash
python save_data_from_CSV_to_database.py
```

---

## Expected Output

The `save_data_from_CSV_to_database.py` script will display execution times for both runs:

```
Script without PRAGMA optimization:
Import completed in X.XX seconds

Script with PRAGMA optimization:
Import completed in Y.YY seconds
```

The second execution (with PRAGMA optimizations) should be noticeably faster for large datasets.

---

## PRAGMA Optimization Details

The script modifies the following PRAGMA settings during the optimized run:

- **`synchronous = OFF`**: Reduces write latency by disabling synchronization after each transaction.
- **`journal_mode = MEMORY`**: Uses in-memory journaling instead of disk-based, speeding up write operations.
- **`cache_size = 100000`**: Increases the memory cache size to store more data in RAM, reducing disk I/O.

At the end of the script, the PRAGMA settings are reset to their default values.

---

## License

This project is licensed under the MIT License.