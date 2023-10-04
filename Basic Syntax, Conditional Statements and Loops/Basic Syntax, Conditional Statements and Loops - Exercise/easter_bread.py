budget = float(input())
price_flour = float(input())
counter = 0
count_eggs = 0
count_breads = 0

price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) / 4

price_one_bread = price_flour + price_eggs + price_milk

while budget - price_one_bread > 0:
    counter += 1
    count_breads += 1
    count_eggs += 3

    budget -= price_one_bread

    if counter == 3:
        count_eggs -= count_breads - 2
        counter = 0

print(f"You made {count_breads} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")
