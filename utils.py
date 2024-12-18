import boto3
import datetime

def fetch_metrics():
    # Simulating metrics fetching logic
    metrics = [
        {"name": "appointments_per_hour", "value": 42, "timestamp": datetime.datetime.now()},
        {"name": "common_conditions", "value": "flu", "timestamp": datetime.datetime.now()},
    ]
    print(f"Fetched metrics: {metrics}")
    return metrics

def get_redshift_credentials():
    # Fetch credentials securely (e.g., from AWS Secrets Manager)
    secret_name = "redshift-credentials"
    region_name = "us-east-1"

    client = boto3.client("secretsmanager", region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    return eval(response["SecretString"])
