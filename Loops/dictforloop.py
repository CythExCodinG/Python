student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

for name in student_scores:
    print(name)

for score in student_scores.values():
    print(score)

for name, score in student_scores.items():
    print(f"{name}: {score}")
