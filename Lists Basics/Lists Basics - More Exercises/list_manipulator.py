initial_list = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]

    if action == 'end':
        print(initial_list)
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
            if command[0] == "max":
                max_element = max(filtered_list)
                max_index = len(initial_list) - 1 - initial_list[::-1].index(max_element)
                print(max_index)
            else:
                min_element = min(filtered_list, )
                min_index = len(initial_list) - 1 - initial_list[::-1].index(min_element)
                print(min_index)

    elif action == "first" or action == "last":
        count = int(command[1])
        even_odd = command[2]
        if even_odd == "even":
            filtered_list = [num for num in initial_list if num % 2 == 0]
        else:
            filtered_list = [num for num in initial_list if num % 2 != 0]
        if count > len(initial_list):
            print("Invalid count")
        else:
            if action == "first":
                result = filtered_list[:count]
            else:
                result = filtered_list[-count:]
            if len(result) < count:
                result = filtered_list
            print(result)
            result.clear()
