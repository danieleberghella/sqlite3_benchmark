import sqlite3
import csv
import time
import os

DB_FILE = "database.db"
CSV_FILE = "data.csv"
TABLE_NAME = "employees"

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)


def apply_pragma(cursor):
    cursor.executescript("""
        PRAGMA synchronous = OFF;
        PRAGMA journal_mode = MEMORY;
        PRAGMA cache_size = 100000;
    """)


def reset_pragma(cursor):
    cursor.executescript("""
        PRAGMA journal_mode = DELETE;
        PRAGMA synchronous = FULL;
        PRAGMA cache_size = 2000;
        PRAGMA vacuum;
    """)


def check_pragma(cursor):
    for pragma in ["synchronous", "journal_mode", "cache_size", "locking_mode"]:
        cursor.execute(f"PRAGMA {pragma};")
        print(f"PRAGMA {pragma}: {cursor.fetchone()[0]}")


def create_table(cursor):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            salary REAL
        )
    """)


def import_csv_to_sqlite(db_file, csv_file, use_pragma=True):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    print("\nPragma Before Changing:")
    check_pragma(cursor)

    if use_pragma:
        print("\nApplying PRAGMA settings...")
        apply_pragma(cursor)
        print("\nPragma After Changing:")
        check_pragma(cursor)

    create_table(cursor)
    cursor.execute(f"DELETE FROM {TABLE_NAME}")
    conn.commit()

    start_time = time.time()
    print("\nImporting data...")

    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for i, row in enumerate(reader, start=1):
            cursor.executemany(f"INSERT INTO {TABLE_NAME} (id, name, age, salary) VALUES (?, ?, ?, ?)", [row])
            conn.commit()

    print(f"\nImport completed in {time.time() - start_time:.2f} seconds")

    if use_pragma:
        reset_pragma(cursor)

    conn.close()


if __name__ == "__main__":
    print("\nScript without PRAGMA optimization:")
    import_csv_to_sqlite(DB_FILE, CSV_FILE, use_pragma=False)
    print("\nScript with PRAGMA optimization:")
    import_csv_to_sqlite(DB_FILE, CSV_FILE, use_pragma=True)
