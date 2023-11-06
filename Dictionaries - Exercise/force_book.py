force_side_dictionary = {}
commands = input()


while commands != "Lumpawaroo":

    if "|" in commands:
        force_side, force_user = commands.split(" | ")
        user_found = False

        for value in force_side_dictionary.values():
            if force_user in value:
                user_found = True
                break
        if not user_found:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)

    elif "->" in commands:
        force_user, force_side = commands.split(" -> ")

        print(f"{force_user} joins the {force_side} side!")

    commands = input()




