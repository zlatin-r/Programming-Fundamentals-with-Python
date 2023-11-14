text = input()
encryption = ""

for letter in text:
    encryption += chr(ord(letter) + 3)

print(encryption)
