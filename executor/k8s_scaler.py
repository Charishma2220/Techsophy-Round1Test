import os
from datetime import datetime
import pandas as pd

LOG_FILE = "scaling_history.csv"

def log_action(action):
    current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"timestamp": current, "action": action}
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame([entry])
    else:
        df = pd.read_csv(LOG_FILE)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    df.to_csv(LOG_FILE, index=False)

def execute_scaling(action):
    # Log the action regardless of what it is
    log_action(action)

    # Optional actual (or simulated) execution
    if action == "scale_up":
        print("🔼 Simulated scaling UP: increasing replicas.")
    elif action == "scale_down":
        print("🔽 Simulated scaling DOWN: decreasing replicas.")
    else:
        print("⏸️ Holding current replica count.")
