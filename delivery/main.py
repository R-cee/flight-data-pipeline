from flask import Flask, jsonify, request
from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# PostgreSQL connection URL
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

@app.route("/aggregated-flights", methods=["GET"])
def get_aggregated_flights():
    try:
        year = request.args.get("year")
        quarter = request.args.get("quarter")

        query = "SELECT * FROM aggregated_flight_data"
        conditions = []
        if year:
            conditions.append(f"year = {int(year)}")
        if quarter:
            conditions.append(f"quarter = {int(quarter)}")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        df = pd.read_sql(query, con=engine)
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
