import re

pattern = r".*@([A-Za-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*"

lines = int(input())
attacked_planets = []
destroyed_planets = []

for i in range(lines):
    message = input()

    decryption_key = sum(message.lower().count(char) for char in "star")
    decrypted_message = "".join(chr(ord(char) - decryption_key) for char in message)

    decrypted_data = re.search(pattern, decrypted_message)
    if decrypted_data:
        planet_name, planet_population, attack_type, soldier_count = decrypted_data.groups()

        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
