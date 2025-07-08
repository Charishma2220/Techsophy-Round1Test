def decide_action(predicted_cpu_list):
    avg_predicted = sum(predicted_cpu_list) / len(predicted_cpu_list)
    if avg_predicted > 80:
        return "scale_up"
    elif avg_predicted < 30:
        return "scale_down"
    else:
        return "hold"