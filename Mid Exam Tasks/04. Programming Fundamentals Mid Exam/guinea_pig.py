food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

food *= 1000
hay *= 1000
cover *= 1000
weight *= 1000

for day in range(1, 31):
    food -= 300

    if food <= 0:
        print("Merry must go to the pet store!")
        break

    if day % 2 == 0:
        hay_needed = food * 0.05
        hay -= hay_needed
        if hay <= 0:
            print("Merry must go to the pet store!")
            break

    if day % 3 == 0:
        cover_needed = weight / 3
        cover -= cover_needed
        if cover <= 0:
            print("Merry must go to the pet store!")
            break

if food >= 0 and hay >= 0 and cover >= 0:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
