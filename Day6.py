def classify(score):
    if score >= 90:
        return "- Excellent"
    elif score >= 75:
        return "- Good"
    elif score >= 50:
        return "- Average"
    else:
        return "- Fail"

scores = [95, 78, 45, 88, 60]
for score in scores:
    print(score, classify(score))