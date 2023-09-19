initial_list = list(map(int, input().split()))
commands = []

while True:
    command = input()
    if command == "end":
        break
    commands.append(command)

final_list = initial_list.copy()

for command in commands:
    if "exchange" in command:
        index = int(command.split()[1])
        if 0 <= index < len(final_list):
            final_list = final_list[index + 1:] + final_list[:index + 1]
        else:
            print("Invalid index")
    elif "max even" in command:
        max_even_index = -1
        max_even_value = float('-inf')
        for i in range(len(final_list)):
            if final_list[i] % 2 == 0 and final_list[i] >= max_even_value:
                max_even_value = final_list[i]
                max_even_index = i
        if max_even_index != -1:
            print(max_even_index)
        else:
            print("No matches")
    elif "max odd" in command:
        max_odd_index = -1
        max_odd_value = float('-inf')
        for i in range(len(final_list)):
            if final_list[i] % 2 == 1 and final_list[i] >= max_odd_value:
                max_odd_value = final_list[i]
                max_odd_index = i
        if max_odd_index != -1:
            print(max_odd_index)
        else:
            print("No matches")
    elif "min even" in command:
        min_even_index = -1
        min_even_value = float('inf')
        for i in range(len(final_list)):
            if final_list[i] % 2 == 0 and final_list[i] <= min_even_value:
                min_even_value = final_list[i]
                min_even_index = i
        if min_even_index != -1:
            print(min_even_index)
        else:
            print("No matches")
    elif "min odd" in command:
        min_odd_index = -1
        min_odd_value = float('inf')
        for i in range(len(final_list)):
            if final_list[i] % 2 == 1 and final_list[i] <= min_odd_value:
                min_odd_value = final_list[i]
                min_odd_index = i
        if min_odd_index != -1:
            print(min_odd_index)
        else:
            print("No matches")
    elif "first" in command:
        count = int(command.split()[1])
        if count > len(final_list):
            print("Invalid count")
        else:
            elements = [str(x) for x in final_list if (x % 2 == 0 and "even" in command) or (x % 2 == 1 and "odd" in command)]
            print(f"[{', '.join(elements[:count])}]")
    elif "last" in command:
        count = int(command.split()[1])
        elements = [str(x) for x in reversed(final_list) if (x % 2 == 0 and "even" in command) or (x % 2 == 1 and "odd" in command)]
        print(f"[{', '.join(elements[:count])}]")

print(f"[{', '.join(map(str, final_list))}]")
r