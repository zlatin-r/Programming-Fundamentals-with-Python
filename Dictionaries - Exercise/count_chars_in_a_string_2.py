words = [character for character in input() if character != " "]
dictionary = {}

for letter in words:
    if letter not in dictionary:
        dictionary[letter] = 0
    dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
