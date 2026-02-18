# Anomaly detection
def validate_heartbeat(rate):
    """Anomaly detection (high/low heart rate)."""
    if rate < 50:
        return "BRADYCARDIA" # Abnormally slow
    elif rate > 110:
        return "TACHYCARDIA" # Abnormally fast
    else:
        return "NORMAL"
