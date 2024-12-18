from scheduler import run_scheduled_jobs

def main():
    print("Starting the Aggregator Service...")
    run_scheduled_jobs()

if __name__ == "__main__":
    main()
