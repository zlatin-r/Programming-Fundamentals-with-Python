deck = input().split(" ")
shuffles = int(input())

first = [deck[0]]
last = deck[-1]
new_deck = deck[1:-1]

for i in range(shuffles):
    mid = len(new_deck) // 2
    first_half = new_deck[:mid]
    second_half = new_deck[mid:]
    shuffled_deck = []

    for j in range(mid):
        shuffled_deck.append(second_half[j])
        shuffled_deck.append(first_half[j])
    new_deck = shuffled_deck

new_deck.append(last)
first.extend(new_deck)
print(first)
