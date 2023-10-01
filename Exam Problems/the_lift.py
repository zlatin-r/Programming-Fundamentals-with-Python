total_people = int(input())
lift = [int(x) for x in input().split(" ")]
counter = 0
is_full = False

for cabin in lift:
    free_seats = 4 - cabin
    if free_seats > 0:
        if total_people >= 4:
            total_people -= free_seats
            people_seated = 4 - cabin
            lift[counter] = 4
        else:
            lift[counter] = total_people
            total_people = 0
    counter += 1


if set(lift) == {4}:
    is_full = True

if total_people == 0 and is_full is False:
    print("The lift has empty spots!")
    print(" ".join([str(x) for x in lift]))
elif total_people > 0 and is_full:
    print(f"There isn't enough space! {total_people} people in a queue!")
    print(" ".join([str(x) for x in lift]))
else:
    print(" ".join([str(x) for x in lift]))

