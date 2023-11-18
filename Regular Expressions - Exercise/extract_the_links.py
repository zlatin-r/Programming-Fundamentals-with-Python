import re

pattern = r"(www\.[A-Za-z0-9\-?]+\.[a-z\.?]+)"
text = input()

while text:
    match = re.search(pattern, text)
    if match:
        link = match.group(1)
        print(link)
    text = input()
