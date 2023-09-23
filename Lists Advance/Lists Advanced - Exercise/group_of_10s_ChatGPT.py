# Read the input sequence of numbers as a string
numbers = input().split(', ')

# Initialize the group boundary
group_boundary = 10

# Loop until the input list is empty
while numbers:
    # Initialize an empty list to store the current group
    current_group = []

    # Iterate through the input list and add numbers that belong to the current group
    for num in numbers:
        if int(num) <= group_boundary:
            current_group.append(int(num))

    # Remove the numbers that belong to the current group from the input list
    numbers = [num for num in numbers if int(num) > group_boundary]

    # Check if the current group is not empty, and print it
    if current_group:
        print(f"Group of {group_boundary}'s: {current_group}")

    # Increase the group boundary by 10 for the next iteration
    group_boundary += 10
