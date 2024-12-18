from apscheduler.schedulers.blocking import BlockingScheduler
from redshift_client import insert_aggregated_data
from utils import fetch_metrics

def scheduled_task():
    print("Running scheduled aggregation task...")
    metrics = fetch_metrics()
    insert_aggregated_data(metrics)

def run_scheduled_jobs():
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_task, 'interval', hours=1)  # Run every hour
    print("Scheduler started. Running tasks every hour.")
    scheduler.start()
