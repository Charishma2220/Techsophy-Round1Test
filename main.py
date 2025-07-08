from monitoring.metrics_collector import get_metrics
from prediction.forecast import forecast_load
from decision_engine.scaling_policy import decide_action
from executor.k8s_scaler import execute_scaling

def main():
    metrics = get_metrics()
    prediction = forecast_load(metrics)
    action = decide_action(prediction)
    execute_scaling(action)

if __name__ == "__main__":
    main()