days_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
collected_plunder = 0

for day in range(1, days_plunder + 1):
    collected_plunder += daily_plunder

    if day % 3 == 0:
        extra_plunder = daily_plunder / 2
        collected_plunder += extra_plunder
    if day % 5 == 0:
        collected_plunder *= 0.70

if collected_plunder >= expected_plunder:
    print(f"Ahoy! {collected_plunder:.2f} plunder gained.")
else:
    percentage = (collected_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")

