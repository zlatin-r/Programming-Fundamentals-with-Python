animals = input().split(", ")
count = 0

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(animals)-1, -1, -1):
        if animals[i] == "wolf":
            break
        count += 1
    print(f"Oi! Sheep number {count}! You are about to be eaten by a wolf!")
