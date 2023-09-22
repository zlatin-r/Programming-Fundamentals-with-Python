text = input()

result = [x for x in text if x not in 'aeiouAEIOU']

print("".join(result))