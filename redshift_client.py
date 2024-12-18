import psycopg2
from shared.config import Config

def connect_to_redshift():
    conn = psycopg2.connect(
        dbname=Config.REDSHIFT_DB,
        user=Config.REDSHIFT_USER,
        password=Config.REDSHIFT_PASSWORD,
        host=Config.REDSHIFT_HOST,
        port=Config.REDSHIFT_PORT
    )
    return conn


def insert_aggregated_data(metrics):
    conn = connect_to_redshift()
    try:
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
        conn.rollback()
    finally:
        conn.close()
