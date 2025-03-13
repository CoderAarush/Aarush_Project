from datetime import date
y = int(input("Please enter year:"))
m = int(input("Please enter month:"))
d = int(input("Please enter day:"))

y2 = int(input("Please enter year:"))
m2 = int(input("Please enter month:"))
d2 = int(input("Please enter day:"))

f_date = date(y, m, d)
l_date = date(y2, m2, d2)
delta = l_date - f_date
print(delta.days)