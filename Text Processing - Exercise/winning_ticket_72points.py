tickets = [ticket.strip() for ticket in input().split(", ")]
winning_chars = ["@", "#", "$", "^"]
match = ""


def valid_check(ticket):
    if len(ticket) == 20:
        return True


def winning_check(ticket):
    global match
    left_side = ticket[:10]
    right_side = ticket[10:]
    for char in winning_chars:
        if char * 6 in left_side and char * 6 in right_side:
            match = char
            return True


def jackpot_check(ticket):
    global match
    for char in winning_chars:
        if char in ticket and len(set(ticket)) == 1:
            match = char
            return True


for ticket in tickets:
    if valid_check(ticket) and jackpot_check(ticket):
        print(f'ticket "{ticket}" - {10}{match} Jackpot!')
    elif valid_check(ticket) and winning_check(ticket):
        print(f'ticket "{ticket}" - {6}{match}')
    elif valid_check(ticket):
        print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")
