from pyspark.sql import SparkSession
from database import get_postgres_jdbc_url
from transformations import clean_and_aggregate

def main():
    # Start Spark
    spark = SparkSession.builder \
        .appName("FlightDataProcessing") \
        .config("spark.jars.packages", "org.postgresql:postgresql:42.2.27") \
        .getOrCreate()

    jdbc_url, jdbc_options = get_postgres_jdbc_url()

    # Read raw flight data from PostgreSQL
    df = spark.read.format("jdbc") \
        .option("url", jdbc_url) \
        .option("dbtable", "raw_flight_data") \
        .options(**jdbc_options) \
        .load()

    aggregated_df = clean_and_aggregate(df)

    # Write results back to PostgreSQL
    aggregated_df.write.format("jdbc") \
        .option("url", jdbc_url) \
        .option("dbtable", "aggregated_flight_data") \
        .mode("overwrite") \
        .options(**jdbc_options) \
        .save()

    print("Aggregated data written to 'aggregated_flight_data'")
    spark.stop()

if __name__ == "__main__":
    main()
