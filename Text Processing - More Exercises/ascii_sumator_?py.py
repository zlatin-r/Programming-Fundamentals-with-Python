start_char, end_char, random_string = input(), input(), input()

print(sum([ord(char) for char in random_string if ord(start_char) < ord(char) < ord(end_char)]))