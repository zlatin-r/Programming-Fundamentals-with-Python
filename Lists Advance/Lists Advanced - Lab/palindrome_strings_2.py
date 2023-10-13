words = input().split()
word = input()

filtered = [x for x in words if x == x[::-1]]

print(filtered)
print(f"Found palindrome {filtered.count(word)} times")
