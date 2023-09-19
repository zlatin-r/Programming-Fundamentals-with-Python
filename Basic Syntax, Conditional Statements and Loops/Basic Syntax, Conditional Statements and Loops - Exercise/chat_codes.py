n = int(input())
message = ""

for i in range(n):
    num = int(input())

    if num == 88:
        message = "Hello"
    elif num == 86:
        message = "How are you?"
    elif num > 88:
        message = "Bye."
    else:
        message = "GREAT!"
    print(message)
