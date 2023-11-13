usernames = input().split(", ")


def len_check(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def alpha_num_check(name):
    for letter in name:
        if not (letter.isalnum() \
                or letter == "-" \
                or letter == "_"):
            return False
    return True


def space_check(name):
    if " " in name:
        return False
    return True


def is_valid(name):
    if len_check(name) and space_check(name) and alpha_num_check(name):
        return True
    return False


for name in usernames:
    if is_valid(name):
        print(name)
