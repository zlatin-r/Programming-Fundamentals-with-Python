num_people = int(input())
capacity = int(input())
count = 0

while num_people > 0:
    num_people -= capacity
    count += 1

print(count)