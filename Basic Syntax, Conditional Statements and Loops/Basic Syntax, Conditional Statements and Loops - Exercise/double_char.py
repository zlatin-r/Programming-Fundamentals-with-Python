string = input()

while string != "End":
    result = ""

    if string == "SoftUni":
        pass
    else:
        for i in range(len(string)):
            result += string[i] * 2
        print(result)

    string = input()
