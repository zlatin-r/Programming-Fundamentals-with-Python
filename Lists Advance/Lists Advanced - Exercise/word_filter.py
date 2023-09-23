text = input().split(" ")

filtered_text = [x for x in text if len(x) % 2 == 0]
for word in filtered_text:
    print(word)
