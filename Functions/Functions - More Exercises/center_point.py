from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def center_point():
    rate_point_one = abs(x1) + abs(y1)
    rate_point_two = abs(x2) + abs(y2)

    if rate_point_one > rate_point_two:
        print(f"({floor(x2)}, {floor(y2)})")
    elif rate_point_one < rate_point_two:
        print(f"({floor(x1)}, {floor(y1)})")
    else:
        print(f"({floor(x1)}, {floor(y1)})")


center_point()
