lines = int(input())
word = input()
lst = []
lls_2 = []

for _ in range(lines):
    string = input()

    lst.append(string)
    if word in string:
        lls_2.append(string)

print(lst)
print(lls_2)
