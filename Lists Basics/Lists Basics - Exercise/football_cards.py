A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards = input().split(" ")
flag = False

for i in range(len(cards)):

    if "A" in cards[i]:
        if int(cards[i][2::]) in A:
            A.remove(int(cards[i][2::]))
        else:
            continue

    if "B" in cards[i]:
        if int(cards[i][2::]) in B:
            B.remove(int(cards[i][2::]))
        else:
            continue

    if len(A) < 7 or len(B) < 7:
        flag = True
        break

if flag:
    print(f"Team A - {len(A)}; Team B - {len(B)}")
    print("Game was terminated")
else:
    print(f"Team A - {len(A)}; Team B - {len(B)}")
