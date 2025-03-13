print("Please enter amount, rate of interst, and years")
amt = float(input())
ri = float(input())
t = float(input())
ri2 = (amt/100)*ri
future_amount = amt + (ri2*t)
future_profit = future_amount - amt
print(amt,"amount with rate of interest",ri,"and time",t,"is equal to",future_amount,"with profit", future_profit)



