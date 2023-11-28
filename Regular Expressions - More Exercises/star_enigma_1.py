import re

num_messages = int(input())
pattern = r"@([A-Za-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*!([AD])![^\@\-\!\:\>]*->(\d+)"
data = {"D": [], "A": []}

for _ in range(num_messages):
    encrypted_message = input()
    key = len(re.findall(r"[star]", encrypted_message, re.I))
    decrypted_message = "".join([chr(ord(encrypted_message[char]) - key) for char in range(len(encrypted_message))])
    match = re.search(pattern, decrypted_message)

    if match:
        planet, population, action, soldiers = match.groups()
        if planet not in data.values():
            data[action].append(planet)

print(f"Attacked planets: {len(data['A'])}")
for planet in sorted(data["A"]):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(data['D'])}")
for planet in sorted(data["D"]):
    print(f"-> {planet}")
