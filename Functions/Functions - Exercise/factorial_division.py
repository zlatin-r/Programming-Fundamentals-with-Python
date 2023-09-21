first_number = int(input())
second_number = int(input())


def fact_division():
    first_fact = first_number
    second_fact = second_number

    for i in range(first_number - 1, 0, -1):
        first_fact *= i
    for i in range(second_number - 1, 0, -1):
        second_fact *= i

    result = first_fact / second_fact
    print(f"{result:.2f}")


fact_division()
