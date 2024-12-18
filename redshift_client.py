import psycopg2
import traceback
from shared.config import Config

def connect_to_redshift():
    try:
        conn = psycopg2.connect(
            dbname=Config.dev,
            user=Config.awsuser,
            password=Config.Admin$100,
            host="healthsync-metrics.c9oyzhxa9puz.eu-north-1.redshift.amazonaws.com",
            port=5439
        )
        return conn
    except Exception as e:
        print(f"Error connecting to Redshift: {e}")
        raise  # Reraise the exception after logging

def insert_aggregated_data(metrics):
    conn = None
    try:
        conn = connect_to_redshift()
        with conn.cursor() as cur:
            for metric in metrics:
                cur.execute(
                    """
                    INSERT INTO aggregated_metrics (metric_name, metric_value, timestamp)
                    VALUES (%s, %s, %s)
                    """,
                    (metric["name"], metric["value"], metric["timestamp"])
                )
        conn.commit()
        print("Metrics inserted successfully.")
    except Exception as e:
        print(f"Error inserting metrics: {e}")
        print(traceback.format_exc())
        if conn:
            conn.rollback()  # Ensure rollback if something goes wrong
    finally:
        if conn:
            conn.close()  # Close connection after commit or rollback
