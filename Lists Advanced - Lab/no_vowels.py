text = input()

result = [x for x in text if x not in 'aeiou']

print("".join(result))