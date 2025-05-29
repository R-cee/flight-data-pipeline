from database import get_engine
from loader import load_csv_to_postgres

def main():
    engine = get_engine()
    csv_path = "ingestion/data/flight_data.csv"
    table_name = "raw_flight_data"

    load_csv_to_postgres(csv_path, table_name, engine)

if __name__ == "__main__":
    main()
