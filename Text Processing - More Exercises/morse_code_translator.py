code = input()
translation = ""
morse_alphabet = {
    '.-': 'A', '-.': 'N',
    '-...': 'B', '---': 'O',
    '-.-.': 'C', '.--.': 'P',
    '-..': 'D', '--.-': 'Q',
    '.': 'E', '.-.': 'R',
    '..-.': 'F', '...': 'S',
    '--.': 'G', '-': 'T',
    '....': 'H', '..-': 'U',
    '..': 'I', '...-': 'V',
    '.---': 'J', '.--': 'W',
    '-.-': 'K', '-..-': 'X',
    '.-..': 'L', '-.--': 'Y',
    '--': 'M', '--..': 'Z',
}

letters = code.split()
for letter in letters:
    if letter == "|":
        translation += " "
    else:
        translation += morse_alphabet[letter]
print(translation)
