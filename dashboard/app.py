import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import time
from datetime import datetime


from prediction.forecast import forecast_load
from monitoring.metrics_collector import get_metrics
from decision_engine.scaling_policy import decide_action
from executor.k8s_scaler import execute_scaling

st.set_page_config(page_title="Smart Auto-Scaler", layout="wide")
st.title("🚀 Smart Auto-Scaling Dashboard")

# Empty container to refresh the display
placeholder = st.empty()

while True:
    with placeholder.container():
        # 1. Collect current metrics
        metrics = get_metrics()

        # 2. Predict future load
        predictions = forecast_load(metrics)

        # 3. Make scaling decision
        decision = decide_action(predictions)

        # 4. Execute scaling action
        execute_scaling(decision)

        # 5. Display metrics
        st.subheader("📊 Current System Metrics")
        st.json(metrics)

        # 6. Display prediction chart
        st.subheader("🔮 Predicted CPU Usage (%)")
        df = pd.DataFrame({'Time': list(range(len(predictions))), 'Predicted CPU': predictions})
        st.line_chart(df.set_index("Time"))

        # 7. Display scaling decision
        st.subheader("⚙️ Scaling Decision")
        st.success(f"Action Taken: **{decision.upper()}**")

        # 8. Show history chart
        st.subheader("📈 Scaling History (Last 20 decisions)")
        try:
            past_df = pd.read_csv("scaling_history.csv").tail(20)
            past_df['timestamp'] = pd.to_datetime(past_df['timestamp'])
            past_df['count'] = 1
            chart_data = past_df.groupby(['timestamp', 'action']).count().reset_index()
            pivot = chart_data.pivot(index='timestamp', columns='action', values='count').fillna(0)
            st.bar_chart(pivot)
        except FileNotFoundError:
            st.info("No scaling history found.")

    # Refresh every 10 seconds
    time.sleep(10)
