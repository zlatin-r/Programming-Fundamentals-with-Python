number_of_electrons = int(input())
full_shells = []
shell_count = 1

while number_of_electrons > 0:
    max_el_in_shell = 2 * shell_count ** 2

    if max_el_in_shell > number_of_electrons:
        full_shells.append(number_of_electrons)
        break
    else:
        full_shells.append(max_el_in_shell)
        number_of_electrons -= max_el_in_shell
    shell_count += 1

print(full_shells)
