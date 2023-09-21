password = input()


def pass_check(password):
    flag = True

    if not (6 <= len(password) <= 10):
        flag = False
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        flag = False
        print("Password must consist only of letters and digits")

    if sum(1 for char in password if char.isdigit()) < 2:
        flag = False
        print("Password must have at least 2 digits")

    if flag:
        print("Password is valid")

    exit()


print(pass_check(password))
