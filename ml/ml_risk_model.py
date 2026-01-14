import numpy as np
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

X_train = np.array([
    [1, 30],
    [2, 60],
    [3, 90],
    [1, 40]
])
y_train = [0, 0, 1, 0]

model.fit(X_train, y_train)

def ml_risk_prediction(indicators_count, risk_score):
    prob = model.predict_proba([[indicators_count, risk_score]])
    return round(prob[0][1] * 100, 2)
