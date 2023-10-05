the_neighborhood = list(map(int, input().split("@")))

jump_command = input()
jump_position = 0


def jump_neighborhood(length_dis):
    global jump_position
    jump_position += length_dis
    if jump_position >= len(the_neighborhood):
        jump_position = 0

    if the_neighborhood[jump_position] == 0:
        print(f"Place {jump_position} already had Valentine's day.")
    else:
        the_neighborhood[jump_position] -= 2
        if the_neighborhood[jump_position] == 0:
            print(f"Place {jump_position} has Valentine's day.")


while jump_command != "Love!":
    jump_command = jump_command.split()
    jump_neighborhood(int(jump_command[1]))

    jump_command = input()

print(f"Cupid's last position was {jump_position}.")

if sum(the_neighborhood) == 0:
    print("Mission was successful.")
else:
    fail_count = the_neighborhood.count(0)
    print(f"Cupid has failed {len(the_neighborhood) - fail_count} places.")
