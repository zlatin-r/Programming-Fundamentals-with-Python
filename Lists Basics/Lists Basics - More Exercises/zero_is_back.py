lst = input().split(", ")

for i in lst:
    if int(i) == 0:
        lst.remove(i)
        lst.extend(i)
print(list(map(int, lst)))
