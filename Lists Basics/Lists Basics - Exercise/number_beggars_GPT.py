numbers = input().split(", ")
n = int(input())

# Initialize a list to store the sums for each beggar
sums = [0] * n

# Iterate through the numbers and distribute them among the beggars
for i in range(len(numbers)):
    beggar_index = i % n  # Calculate which beggar should receive the current number
    sums[beggar_index] += int(numbers[i])  # Add the number to the beggar's sum

print(sums)
