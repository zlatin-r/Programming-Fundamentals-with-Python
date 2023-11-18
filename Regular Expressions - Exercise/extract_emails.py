import re

string = input()

pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

matches = re.findall(pattern, string)

for mail in matches:
    print(mail[0])
