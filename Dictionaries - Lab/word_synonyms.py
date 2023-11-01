n = int(input())
synonyms = {}

for _ in range(n):
    key_word = input()
    synonym = input()

    if key_word not in synonyms:
        synonyms[key_word] = []
    synonyms[key_word].append(synonym)

for word in synonyms:
    print(f"{word} - {'. '.join(synonyms[word])}")
