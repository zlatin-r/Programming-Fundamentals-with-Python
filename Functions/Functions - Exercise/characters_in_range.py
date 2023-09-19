a = input()
b = input()
result = []


def char_range(a, b):
    for i in range(ord(a) + 1, ord(b)):
        result.append(chr(i))
    return " ".join(result)


print(char_range(a, b))
