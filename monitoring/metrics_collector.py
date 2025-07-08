import random
import time
from datetime import datetime

def get_metrics():
    cpu = random.randint(40, 95)
    memory = random.randint(50, 90)
    rps = random.randint(100, 600)
    latency = random.randint(100, 500)

    return {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cpu_usage': cpu,
        'memory_usage': memory,
        'requests_per_second': rps,
        'latency': latency
    }

def stream_metrics(duration_secs=60, to_csv=False):
    print("Streaming simulated metrics:\n")
    records = []
    for _ in range(duration_secs):
        data = get_metrics()
        print(data)
        records.append(data)
        time.sleep(1)

    if to_csv:
        import pandas as pd
        df = pd.DataFrame(records)
        df.to_csv("simulated_metrics.csv", index=False)
        print("\nSaved to simulated_metrics.csv ✅")

if __name__ == "__main__":
    stream_metrics(duration_secs=60, to_csv=True)