num_city = int(input())
total_earned_money = 0

for city in range(1, num_city + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())

    if city % 5 == 0:
        losses = income * 0.10
        income -= losses

    elif city % 3 == 0:
        additional_costs = expenses * 0.50
        expenses += additional_costs

    income -= expenses
    total_earned_money += income

    print(f"In {city_name} Burger Bus earned {income:.2f} leva.")

print(f"Burger Bus total profit: {total_earned_money:.2f} leva.")
