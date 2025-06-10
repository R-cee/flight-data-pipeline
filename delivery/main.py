from flask import Flask, jsonify, request, send_file
from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv
import io

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
        output_format = request.args.get("format", "json").lower()

        query = """
            SELECT 
                from_airport_code, 
                dest_airport_code, 
                year, 
                quarter, 
                avg_co2_emission
            FROM aggregated_flight_data
        """
        conditions = []
        params = {}
        if year:
            conditions.append("year = :year")
            params["year"] = int(year)
        if quarter:
            conditions.append("quarter = :quarter")
            params["quarter"] = int(quarter)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        df = pd.read_sql(text(query), con=engine, params=params)

        if output_format == "csv":
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)
            return send_file(
                io.BytesIO(csv_buffer.getvalue().encode()),
                mimetype='text/csv',
                as_attachment=True,
                download_name='aggregated_flights.csv'
            )
        else:
            return jsonify(df.to_dict(orient="records"))

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
