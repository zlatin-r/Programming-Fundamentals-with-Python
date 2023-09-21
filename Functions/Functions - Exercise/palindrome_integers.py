numbers = input().split(", ")


def palindrome_check():
    for i in numbers:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


palindrome_check()
