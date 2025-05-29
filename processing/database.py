import os
from dotenv import load_dotenv

load_dotenv()

def get_postgres_jdbc_url():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    return f"jdbc:postgresql://{host}:{port}/{db}", {"user": user, "password": password, "driver": "org.postgresql.Driver"}
