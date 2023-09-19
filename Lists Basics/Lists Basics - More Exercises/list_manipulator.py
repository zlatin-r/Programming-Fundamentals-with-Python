initial_list = list(map(int, input().split()))
max_min_index = 0
max_min_el = 0
prev = len(initial_list)

while True:
    command = input().split()
    action = command[0]

    if action == 'end':
        break

    elif action == 'exchange':
        index = int(command[1])
        if 0 <= index < len(initial_list):
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]
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
                max_min_index = initial_list[::-1].index(max(filtered_list))
            else:
                max_min_index = initial_list[::-1].index(min(filtered_list))
            print(initial_list[::-1].index(len(initial_list) - max_min_index))
            print(initial_list.index(max_min_index))
