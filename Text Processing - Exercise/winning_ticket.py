tickets = [ticket.strip() for ticket in input().split(", ")]
symbols = ('@', '#', '$', '^')


def check(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_part = ticket[:10]
    right_part = ticket[10:]

    for match_symbol in symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_rep = match_symbol * uninterrupted_match_length
            if winning_symbol_rep in left_part and winning_symbol_rep in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


for ticket in tickets:
    print(check(ticket))
