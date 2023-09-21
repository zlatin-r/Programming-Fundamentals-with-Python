numbers = input().split(", ")


def is_palindrome(number):
    number == number[::-1]


def check_palindrome(numbers):
    for num in numbers:
        print(is_palindrome(num))