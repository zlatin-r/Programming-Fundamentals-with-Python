n = int(input())

for i in range(97, n + 97):
    for j in range(97, n + 97):
        for k in range(97, n + 97):
            print(chr(i)+chr(j)+chr(k))
