initial_list = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]

    if action == 'end':
        break

    elif action == 'exchange':
        index = int(command[1])
        if 0 <= index < len(initial_list):
            left_sublist = initial_list[:index + 1]
            right_sublist = initial_list[index + 1:]
            initial_list = right_sublist + left_sublist
        else:
            print('Invalid index')

    elif action in ["max", "min"]:
        even_odd = command[1]
        if even_odd == "even":
            filtered_list = [num for num in initial_list if num % 2 == 0]
        else:
            filtered_list = [num for num in initial_list if num % 2 != 0]
        if not filtered_list:
            print("No matches")
        else:
            if action == "max":
                max_min_index = initial_list.index(max(filtered_list))
                print(max_min_index)
            else:
                max_min_index = initial_list.index(min(filtered_list))
                print(max_min_index)
    elif action in ["first", "last"]:
        count = int(command[1])
        even_odd = command[2]
        if even_odd == "even":
            filtered_list = [num for num in initial_list if num % 2 == 0]
        else:
            filtered_list = [num for num in initial_list if num % 2 != 0]

        if len(filtered_list) == 0:
            print(filtered_list)
        elif count > len(filtered_list):
            print("Invalid count")
        else:
            result = filtered_list[:count] if action == "first" else filtered_list[-count:]
            print(result)

    elif action == "end":
        break

print(initial_list)
