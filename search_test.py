question = input("Enter Question: ")

with open("knowledge.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()

question_words = question.lower().split()

results = []

for line in knowledge.split("\n"):

    score = 0

    for word in question_words:

        if word in line.lower():
            score += 1

    if score > 0:
        results.append((score, line))

results.sort(reverse=True)

print("\nTOP RESULTS:\n")

for result in results[:20]:
    print(result[1])