number_of_rooms = int(input())
total_free_chairs = 0
game_on = True

for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split(" ")
    number_of_chairs = int(len(chairs_and_visitors[0]))
    number_of_visitors = int(chairs_and_visitors[1])

    if number_of_chairs < number_of_visitors:
        game_on = False
        needed_chairs_in_room = number_of_visitors - number_of_chairs
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
    else:
        total_free_chairs += number_of_chairs - number_of_visitors

if game_on:
    print(f"Game On, {total_free_chairs} free chairs left")