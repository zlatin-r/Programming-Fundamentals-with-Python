n = int(input())


def tribonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 2]
    else:
        trib = [1, 1, 2]
        for i in range(3, n):
            next_trib = trib[i - 1] + trib[i - 2] + trib[i - 3]
            trib.append(next_trib)
        return trib


def print_tribonacci(n):
    trib_sequence = tribonacci(n)
    print(" ".join(map(str, trib_sequence)))


print_tribonacci(n)
