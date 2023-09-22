words = input().split(" ")
palindrome = input()

words = [word for word in words if word == word[::-1]]

print(words)
print(f"Found palindrome {words.count(palindrome)} times")