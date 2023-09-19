lines = int(input())
positive = []
negative = []

for _ in range(lines):
    number = int(input())

    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
