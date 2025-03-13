def calc_func(par1):
    print("Please enter problem type- buying and selling companies- 1, partially owning companies- 2:")
    par5 = int(input())
    if(par5==1):
        print("Please enter buy price, sell price,: ")
        buy_price = int(input())
        sell_price = int(input())
        p = buy_price/100
        profit = buy_price - sell_price
        p2 = profit/p
        print("In this trade the money made =", profit,"and profit/loss percent =", p2)
    else:
        print("Please enter shares of company bought, buying price, and selling price and also the time held")
        share_qty = int(input())
        buy_price = int(input())
        sell_price = int(input())
        time = int(input())
        investment_value = buy_price*share_qty
        sell_val = sell_price*share_qty
        profit = sell_val - investment_value
        annual_profit = profit/time
        print("In this certain time in your profession your profit/loss was",profit,"with your annual growth/declinati")
        print("on being,", annual_profit)
def calc_func2(par2):
    print("Please enter problem type- shorting- 1, buying- 2 ")
    par6 = int(input())
    if(par6 == 1):
        print("Please enter sell price, buy price and quantity and also time held and even taxes:")
        buy_price = int(input())
        sell_price = int(input())
        qty = int(input())
        t = int(input())
        debt = int(input())
        sell_val = buy_price*qty
        buy_val = sell_price*qty
        profit = buy_val - sell_val-debt
        annual_growth = profit/t
        print("The money made on this trade =",profit,"everyday the average growth was =",annual_growth)
    else:
        print("Please enter but price, sell price and quantity and also time held and also taxes:")
        buy_price = int(input())
        sell_price = int(input())
        qty = int(input())
        t = int(input())
        debt = int(input())
        sell_val = sell_price * qty
        buy_val = buy_price * qty
        profit = buy_val - sell_val-debt
        annual_growth = profit / t
        print("The money made on this trade =", profit, "everyday the average growth was =", annual_growth)
def calac_func3(par3):
    print("Please enter buy price, sell price, holding period and taxes and also quantity:")
    buy_price = int(input())
    sell_price = int(input())
    t = int(input())
    debt = int(input())
    share_qty = int(input())
    buy_val = buy_price*share_qty
    sell_val = sell_price*share_qty
    profit = (sell_val-buy_val)-debt
    annual_growth = profit/t
    print("The money made/lost on this trade =", profit, "annual growth =", annual_growth)
def calc_func4(par4):
    print("Please enter  profits and losses of 3 years(starting from year3 to year1):")
    data_1 = int(input())
    data_2 = int(input())
    data_3 = int(input())
    if(data_1<=data_2<=data_3):
        print("Looking at previous data of this company the algorithims have come to a conclusion that")
        print("may go futher up.In order to bring this analysis to a conclusion please enter if recent events are ")
        print("positve or negative for companies_s growth. If positive enter 1 if negative enter 0:")
        par7 = int(input())
        if(par7==1):
            print("The riask factor in order to execute a buying trade is 3:1 ")
        else:
            print("Risk factotor to execute a shorting trade is 2:1")
    elif (data_1 <= data_3 <= data_2):
        print("Looking at previous data of this company the algorithims have come to a conclusion that", company_name)
        print("may go futher up.In order to bring this analysis to a conclusion please enter if recent events are ")
        print("positve or negative for companies_s growth. If positive enter 1 if negative enter 0:")
        par8 = int(input())
        if (par8 == 1):
            print("The riask factor in order to execute a buying trade is 2:1 ")
        else:
            print("Risk factotor to execute a shorting trade is 1:1")
    elif (data_2 <= data_1 <= data_3):
        print("Looking at previous data of this company the algorithims have come to a conclusion that", company_name)
        print("may go futher up.In order to bring this analysis to a conclusion please enter if recent events are ")
        print("positve or negative for companies_s growth. If positive enter 1 if negative enter 0:")
        par9 = int(input())
        if (par9 == 1):
            print("The riask factor in order to execute a buying trade is 2:1 ")
        else:
            print("Risk factotor to execute a shorting trade is 1:1")
    elif (data_2 <= data_3 <= data_1):
        print("Looking at previous data of this company the algorithims have come to a conclusion that", company_name)
        print("may go futher up.In order to bring this analysis to a conclusion please enter if recent events are ")
        print("positve or negative for companies_s growth. If positive enter 1 if negative enter 0:")
        par10 = int(input())
        if (par10 == 1):
            print("The riask factor in order to execute a buying trade is 2:1 ")
        else:
            print("Risk factotor to execute a shorting trade is 3:1")
    elif (data_3 <= data_2 <= data_1):
        print("Looking at previous data of this company the algorithims have come to a conclusion that", company_name)
        print("may go futher up.In order to bring this analysis to a conclusion please enter if recent events are ")
        print("positve or negative for companies_s growth. If positive enter 1 if negative enter 0:")
        par11 = int(input())
        if (par11 == 1):
            print("The riask factor in order to execute a buying trade is 4:1 ")
        else:
            print("Risk factotor to execute a shorting trade is 3:1")
    else:
        print("Looking at previous data of this company the algorithims have come to a conclusion that")
        print("may go futher up.In order to bring this analysis to a conclusion please enter if recent events are ")
        print("positve or negative for companies_s growth. If positive enter 1 if negative enter 0:")
        par12 = int(input())
        if (par12 == 1):
            print("The riask factor in order to execute a buying trade is 2:1 ")
        else:
            print("Risk factotor to execute a shorting trade is 4:1")
def main():
    print("Please enter problem type - Investment banking- 1, traders- 2, investors- 3,evaluating big companies- 4:")
    problem_type = int(input())
    if(problem_type==1):
        calc_func(problem_type)
    elif(problem_type==2):
        calc_func2(problem_type)
    elif(problem_type==3):
        calac_func3(problem_type)
    else:
        calc_func4(problem_type)
main()

