def calculate_risk_score(severity, indicators_count):
    base_score = {
        "low": 30,
        "medium": 60,
        "high": 80
    }
    return base_score.get(severity, 40) + (indicators_count * 5)
