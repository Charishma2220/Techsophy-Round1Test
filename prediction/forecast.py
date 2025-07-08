import random
from prophet import Prophet
import pandas as pd
from datetime import datetime, timedelta

def forecast_load(latest_metrics):
    now = datetime.now()
    data = []

    base = latest_metrics['cpu_usage']

    # Generate pseudo-random CPU pattern
    for i in range(30):
        ts = now - timedelta(minutes=30 - i)
        y = base + random.uniform(-10, 10)
        y = max(0, min(y, 100)) 
        data.append({'ds': ts, 'y': y})

    df = pd.DataFrame(data)

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=10, freq='min')
    forecast = model.predict(future)

    return forecast['yhat'].tail(10).tolist()
