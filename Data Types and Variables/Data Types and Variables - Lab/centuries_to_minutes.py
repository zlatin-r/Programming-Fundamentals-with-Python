centuries = int(input())

years = round(centuries * 100)
days = int(years * 365.2422)
hours = round(days * 24)
minutes = round(hours * 60)

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
