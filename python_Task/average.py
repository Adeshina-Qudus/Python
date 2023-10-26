def average_score(*scores):
    return sum(scores) / len(scores)


exam_scores = []
for i in range(4):
    score = int(input("enter ya score "))
    exam_scores.append(score)


print(average_score(exam_scores))
print(average_score())