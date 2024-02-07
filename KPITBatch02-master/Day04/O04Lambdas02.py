
lst = list(range(1, 11))
print(f"lst :{lst}")

squares = list(map(lambda x: x ** 2, lst))

print(f"squares :{squares}")


# conversion of currency from rupees to dollars
expenses = [8500, 10000, 32000, 15000, 2500, 6000, 50000]

# assignment
# sort the m     onths based on calendar
months = ['apr', 'aug', 'dec', 'feb', 'mar', 'may', 'nov', 'oct', 'jan', 'jun', 'jul', 'sep']

print("-" * 60)
from calendar import month_abbr
print(list(month_abbr))
res = sorted(months, key=list(map(lambda month: month.lower(),list(month_abbr))).index)
print(f"res :{res}")
