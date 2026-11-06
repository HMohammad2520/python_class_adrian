name = input("Enter Name: ")
print("Scores Example: 20,19,18")
scores = input("Enter Scores: ")

scores = scores.split(",")
scores_sum = 0

for score in scores:
    score = int(score)

    if 0 > score or score > 20:
        print("Invalid Score", score)
        break

    scores_sum = scores_sum + score

else:
    avg = scores_sum / len(scores)
    print("Name:", name)
    print("Avg:", avg)
