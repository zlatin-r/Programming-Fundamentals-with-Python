start = input()
end = input()
string = input()
ord_sum = 0

for i in range(len(string)):
    if ord(start) < ord(string[i]) < ord(end):
        ord_sum += ord(string[i])

print(ord_sum)
