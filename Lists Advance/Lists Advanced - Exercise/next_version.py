first_version = input().split(".")

first_version = [int(x) for x in first_version]
digit = int(f"{first_version[0]}{first_version[1]}{first_version[2]}") + 1
string_version = str(digit)
next_version = f"{string_version[0]}.{string_version[1]}.{string_version[2]}"

print(next_version)
