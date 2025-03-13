def calc_func(par1):
    print("Please enter unit if meter- 1,if km- 2, cm- 3,")
    par5 = int(input())
    if par5 == 1:
        print("Please enter no. of meters")
        c2 = int(input())
        if c2  in range(10, 99):
            deca = c2/10
            deca2 = c2%10
            print("number of decameters",c2," is equal to is",deca,"and meters is equal to", deca2)
        elif c2 in range(100,999):
            hecto = c2/100
            hecto2 = c2%100
            print("number of hectometers",c2," is equal to is",hecto,"and meters  left is equal to", hecto2)
        else:
            km = c2/1000
            k_m_2 = c2%1000
            print("number of km",c2," is equal to is",km,"and meters left is equal to", k_m_2)
    elif par5 == 2:
        print("Please enter number of kilometers")
        x = float(input())
        x in range(2, )
        m = (x/1.6)
        m2 = (x%1.6)
        print(x,"kilometers is equal to",m,"miles and", m2,"kilometres")
    else:
        print("Please enter no. of centimeters")
        c4 = float(input())
        if c4 in range(10, 99):
            decimetere = c4/10
            decimetere_2 = c4%10
            print(c4,"centimeters is equal to",decimetere,"decimetres and", decimetere_2,"centimeters")
        elif c4 in range(100, 99999):
            metre = c4/100
            metere2 = c4%100
            print(c4,"centimetres is equal to",metre,"metres and", c4,"centimeters")
        else:
            f = c4/1000
            f_2 = c4%1000
            print(c4,"centimeteres is equal to", f,"Kilometeres and", f_2,"cm")
def calc_func2(par2):
    print("Please enter unit if grams- 1,if milligrams- 2, kilograms- 3")
    par6 = int(input())
    if par6 == 1:
        print("Please enter number of grams")
        c5 = int(input())
        if c5 in range(10, 99):
            decagram = c5/10
            dec2 = c5%10
            print(c5,"grams is equal to",decagram,"decagrams and", dec2,"grams")
        elif c5 in range(100, 999):
            hectogram = c5/100
            h2 = c5%100
            print(c5,"grams is equal to",hectogram,"hectograms and", h2)
        else:
            k_g = c5/1000
            kg = c5%1000
            print(c5,"grams is equal to",k_g,"kilograms and", kg,"grams")
    elif par6 == 2:
        print("Please enter no. of miligrams")
        c5 = int(input())
        if c5 in range(10, 99):
            decigram = c5/1000
            decec = c5%1000
            print(c5,"mg is equal to", decigram,"grams and", decec,"miligrams")
        elif c5 in range(100, 999):
            hetagram = c5/1000
            hada = c5%1000
            print(c5,"mg is equal to", hetagram,"grams and", hada,"mg")
        elif c5 in range(1000, ):
            grams = c5/1000
            stop_dead_in_your_tracks_FBI = c5%1000
            print(c5,"mg is equal to", grams,"grams and", stop_dead_in_your_tracks_FBI,"mg")
    else:
        print("Please enter no. of kilograms")
        c5 = int(input())
        print("Please enter type of answer required if grams- 1, if mg- 2, if tonnes - 3")
        c6 = int(input())
        if c6 == 1:
            c7 = c5*1000
            c_7 = c5%1000
            print(c7)
        elif c6 == 2:
            c8 = c5*1000000
            c_8 = c5%1000000
            print(c8)
        else:
            c7 = c5/1000
            c_7 = c5%1000
            print(c7)
def clac_func_3(par3):
     print("Please enter unit type- if seconds- 1 and/or/if minutes- 2 or/if hours- 3")
     par6 = int(input())
     if(par6==1):
         print("Please enter number of secs")
         arrest = int(input())
         if arrest in range(60, 3599):
             arrest2 = arrest/60
             arret3 = arrest%60
             print(arrest,"seconds is equal to", arrest2,"minutes and", arret3,"seconds")
         else:
             arrest2 = arrest/3600
             arrest3 = arrest%3600
             print(arrest,"seconds is equal to", arrest2,"hours and", arrest3,"seconds")
     elif par6==2:
         print("Please enter number of minutes:")
         arrest = int(input())
         if arrest in range(60, 1440):
             arrest2 = arrest/60
             arrest3 = arrest%60
             print(arrest,"minutes is equal to", arrest2,"hours and", arrest3,"minutes")
         else:
             arrest2 = arrest/1440
             arrest3 = arrest%1440
             print(arrest,"minutes is equal to", arrest2,"days and", arrest3,"minutes")
     else:
         print("Please enter number of hours:")
         you_are_under_arrest = float(input())
         if you_are_under_arrest in range(24, 148):
             arrest6 = you_are_under_arrest/24
             arrest7 = you_are_under_arrest%24
             print(you_are_under_arrest,"hours is equal to", arrest6,"days and", arrest7,"hours")
         elif you_are_under_arrest in range(149, 720):
             arrest6 = you_are_under_arrest / 148
             arrest7 = you_are_under_arrest % 148
             print(you_are_under_arrest, "hours is equal to", arrest6, "weeks and", arrest7, "hours")
         else:
           arrest6 = you_are_under_arrest / 720
           arrest7 = you_are_under_arrest % 720
           print(you_are_under_arrest, "hours is equal to", arrest6, "months and", arrest7, "hours")
def calc_func_4(par):
    print("Please enter unit type if ml- 1, if/elif/else l- 2")
    right_to_remain_silent = float(input())
    if right_to_remain_silent == 1:
        print("Please enter no. of millilitres")
        conspiracy_to_commit_fraud = float(input())
        if conspiracy_to_commit_fraud in range(1, 999):
            conspiracy_to_commit_fraud_FBI = conspiracy_to_commit_fraud/1000
            print(conspiracy_to_commit_fraud,"is equal to", conspiracy_to_commit_fraud_FBI,"litres")
        elif conspiracy_to_commit_fraud in range(1000, 999999):
            x = conspiracy_to_commit_fraud/1000
            yi_eld = conspiracy_to_commit_fraud%1000
            print(conspiracy_to_commit_fraud,"millilitres is equal to", x,"litres")
        else:
            x = conspiracy_to_commit_fraud/1000000
            y = conspiracy_to_commit_fraud%1000
            print(conspiracy_to_commit_fraud,"millilitres is equal to", x,"kl and", y,"litres")
    else:
         print("Please enter no. of litres")
         criminal = float(input())
         if criminal in range(2, 999):
             k_l = 1000
             x = k_l/criminal
             print(criminal,"litres is equal to", x,"kilolitres")
         else:
             k_l = 1000
             x = criminal/k_l
             print(criminal,"litres is equal to", x,"kilolitres")
def main():
    print("Please enter unit,if distance - 1, if weight - 2, if time- 3, else for volume- 4, units in these categories")
    print("Will be asked later:")
    c = int(input())
    if(c == 1):
        calc_func(c)
    elif(c == 2):
        calc_func2(c)
    elif(c == 3):
        clac_func_3(c)
    else:
        calc_func_4(c)
main()