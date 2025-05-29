import pandas as pd
from sqlalchemy.engine import Engine

def load_csv_to_postgres(csv_path: str, table_name: str, engine: Engine):
    try:
        df = pd.read_csv(csv_path)

        if 'flight_date' not in df.columns or 'co2_emission' not in df.columns:
            raise ValueError("Missing required columns.")

        df['flight_date'] = pd.to_datetime(df['flight_date'], errors='coerce')
        df['scan_date'] = pd.to_datetime(df['scan_date'], errors='coerce')

        if 'co2_percentage' in df.columns:
            df['co2_percentage'] = (
            df['co2_percentage']
            .replace('%', '', regex=True)
    )
        df['co2_percentage'] = pd.to_numeric(df['co2_percentage'], errors='coerce')

        # Write to PostgreSQL
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data loaded into table: {table_name}")

    except Exception as e:
        print("Error occurred during data load:")
        print(e)
