scores = [95, 78, 45, 88, 60]

for score in scores:
    if score >= 90:
        print(score, "- Excellent")
    elif score >= 75:
        print(score, "- Good")
    elif score >= 50:
        print(score, "- Average")
    else:
        print(score, "- Fail")