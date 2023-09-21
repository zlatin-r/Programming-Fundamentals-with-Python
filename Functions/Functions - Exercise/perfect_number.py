number = int(input())


def perfect_check():
    sum_nums = 0

    for i in range(1, number + 1):
        if number % i == 0:
            sum_nums += i
        if sum_nums == number:
            print("We have a perfect number!")
            exit()
    print("It's not so perfect.")
    exit()


perfect_check()
