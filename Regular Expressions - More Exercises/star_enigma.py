import re

star_count = r"[star]"
pattern = r".*@([A-Za-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*"

lines = int(input())
attacked_planets = []
destroyed_planets = []

for i in range(lines):
    decrypted_message = ""
    message = input()

    star_match = re.findall(star_count, message, re.IGNORECASE)
    decryption_key = int(len(star_match))

    for char in range(len(message)):
        decrypted_message += chr(ord(message[char]) - decryption_key)

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
