word = input().lower()
total = 0

for i in range(len(word)):

    if word[i:i + 4] == "sand":
        total += 1
    if word[i:i + 5] == "water":
        total += 1
    if word[i:i + 4] == "fish":
        total += 1
    if word[i:i + 3] == "sun":
        total += 1

print(total)
