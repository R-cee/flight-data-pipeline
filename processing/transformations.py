from pyspark.sql import DataFrame
from pyspark.sql.functions import col, avg, quarter, year

def clean_and_aggregate(df: DataFrame) -> DataFrame:
    df_cleaned = df.dropna(subset=["flight_date", "co2_emission", "from_airport_code", "dest_airport_code"])

    df_enriched = df_cleaned.withColumn("year", year(col("flight_date"))) \
                            .withColumn("quarter", quarter(col("flight_date")))

    df_aggregated = df_enriched.groupBy(
        "from_airport_code",
        "dest_airport_code",
        "year",
        "quarter"
    ).agg(
        avg("co2_emission").alias("avg_co2_emission")
    )

    return df_aggregated
