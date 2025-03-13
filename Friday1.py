import subprocess
from datetime import datetime
from datetime import date
import pytz
import math
def say(text):
    subprocess.call(['say', text])
def matrix_main(bytes):
    today = date.today()
    date2 = date(2021, 10, 14)
    if today == date2:
        say("Hello sir Hope you had or are having a nice day")
        matrix_math()
    else:
        say("Hello sir Hope you had or are having a nice day")
        matrix_math()
def matrix_access():
    say("Hello and welcome to Friday")
    say("Please enter access code to determine identity:")
    password_sequence = input()
    int(password_sequence)
    matrix_main(password_sequence)
def matrix_math():
    say("Friday calculations is starting")
    say("What do you wish to do if calculations- 1 if scientific calculations - 2")
    bytes = int(input())
    if bytes == 1:
        say("What do you wish to calculate if 4 standard operations- 1, algebra - 2 if hcf - 3 if square root 4")
        aarush_is_a_businessman = int(input())
        if aarush_is_a_businessman == 1:
            say("What do you whish to calculate if addition 1 if subtraction 2 if multiplication 3 else 4")
            criminal = int(input())
            if criminal == 1:
                say('Please enter two numbers in two seperate lines:')
                num1 = int(input())
                num2 = int(input())
                sum = num1 + num2
                print (sum)
            elif criminal == 2:
                say('Please enter two numbers in two seperate lines:')
                num1 = int(input())
                num2 = int(input())
                if num1 > num2:
                    gre = num1
                    sme = num2
                else:
                    gre = num2
                    sme = num1
                sum = gre - sme
                print (sum)
            elif criminal == 3:
                say("If you  wish to calculate race to the power - 1, else 2")
                SBK_KILLS_PEOPLE_IN_DOZENS_A_YEAR = int(input())
                if SBK_KILLS_PEOPLE_IN_DOZENS_A_YEAR == 1:
                    say("Please enter number")
                    sbk = int(input())
                    say("Please enter race")
                    CARTELS = int(input())
                    SBK_IS_A_CARTEL = sbk ** CARTELS
                    print (SBK_IS_A_CARTEL)
                else:
                    say("Please enter two numbers:")
                    a = int(input())
                    b = int(input())
                    gTTS = a * b * 1
                    print (gTTS)
            else:
                say("Please enter two numbers to exercise division function")
                gTTS = int(input())
                gTTS2 = int(input())
                if gTTS > gTTS2:
                    gre = gTTS
                    s = gTTS2
                else:
                    gre = gTTS2
                    s = gTTS2
                gr = gre / s
                print(gr)
        elif aarush_is_a_businessman == 2:
            say("Please enter values of variables in the order you wish")
            conspiracy2 = int(input())
            shut_up2 = int(input())
            just_get_out_of_here_2 = int(input())
            say(
                "what operations do you whish to perform if addition - 1 if subtraction - 2 if multipliction - 3 if division - 4")
            abbbbbbbabababababababa = int(input())
            if abbbbbbbabababababababa == 1:
                then = conspiracy2 + just_get_out_of_here_2 + shut_up2
                print (then)
            elif abbbbbbbabababababababa == 2:
                if conspiracy2 > just_get_out_of_here_2 > shut_up2:
                    gre = conspiracy2
                    gre2 = just_get_out_of_here_2
                    s = shut_up2
                elif conspiracy2 > shut_up2 > just_get_out_of_here_2:
                    gre = conspiracy2
                    gre2 = shut_up2
                    s = just_get_out_of_here_2
                elif shut_up2 > conspiracy2 > just_get_out_of_here_2:
                    gre = shut_up2
                    s = just_get_out_of_here_2
                    gre2 = conspiracy2
                elif shut_up2 > just_get_out_of_here_2 > conspiracy2:
                    gre = shut_up2
                    s = conspiracy2
                    gre2 = just_get_out_of_here_2
                elif just_get_out_of_here_2 > conspiracy2 > shut_up2:
                    gre = just_get_out_of_here_2
                    s = shut_up2
                    gre2 = conspiracy2
                else:
                    gre = just_get_out_of_here_2
                    s = conspiracy2
                    gre2 = shut_up2
                then = gre - gre2 - s
                print (then)
            elif abbbbbbbabababababababa == 3:
                then = conspiracy2 * just_get_out_of_here_2 * shut_up2
                print (then)
            else:
                if conspiracy2 > just_get_out_of_here_2 > shut_up2:
                    gre = conspiracy2
                    gre2 = just_get_out_of_here_2
                    s = shut_up2
                elif conspiracy2 > shut_up2 > just_get_out_of_here_2:
                    gre = conspiracy2
                    gre2 = shut_up2
                    s = just_get_out_of_here_2
                elif shut_up2 > conspiracy2 > just_get_out_of_here_2:
                    gre = shut_up2
                    s = just_get_out_of_here_2
                    gre2 = conspiracy2
                elif shut_up2 > just_get_out_of_here_2 > conspiracy2:
                    gre = shut_up2
                    s = conspiracy2
                    gre2 = just_get_out_of_here_2
                elif just_get_out_of_here_2 > conspiracy2 > shut_up2:
                    gre = just_get_out_of_here_2
                    s = shut_up2
                    gre2 = conspiracy2
                else:
                    gre = just_get_out_of_here_2
                    s = conspiracy2
                    gre2 = shut_up2
                then = gre / gre2 / s
                print (then)
        elif aarush_is_a_businessman == 3:
            matrix_hcf()
        elif aarush_is_a_businessman == 4:
            say("Please enter a number:")
            s = int(input())
            s2 = math.sqrt(s)
            print(s2)
    else:
        say("What do you wish to calculate if force 1 if speed 2 if power 3")
        hacking_databases = int(input())
        if hacking_databases == 1:
            say(
                "Please enter weight of object to which force is being applied to in kg if less than use decimal point:")
            mass = int(input())
            say(
                "Please enter starting velocity and final velocity in meter and seconds in two different lines without the slash and space between the two velocitys")
            hack_other_computers = int(input())
            hack_other_computers2 = int(input())
            hack = int(input())
            hack2 = int(input())
            Force_calculated_1 = hack_other_computers / hack_other_computers2
            Force_calculated_2 = hack / hack2
            accelration_1 = Force_calculated_2 - Force_calculated_1
            total_time = hack_other_computers2 + hack2
            accelration = accelration_1 / total_time
            force = mass * accelration
            print(force)
        elif hacking_databases == 2:
            say("Please enter distance as d in kilometres:")
            d = int(input())
            say("Please enter time as t in hours:")
            t = int(input())
            speed = d / t
            print ("The distance travelled in one hour is equal to", speed)
        else:
            say(
                "What do you wish to calculate if watt hour 1 if kilojoules - 2 if joules to watts or the other way around 3")
            i_a = int(input())
            if i_a == 1:
                say("Please enter number of watts the source held for")
                watt_hold = int(input())
                say("Please enter number of hours")
                watt_hour = int(input())
                joules = watt_hour * 3600
                say("The number of joules the source supplied you with is:")
                print(joules)
            elif i_a == 2:
                say("Please enter number of kilojoules:")
                kilojoule = int(input())
                sec = int(input(say("Please enter number of seconds")))
                energy_from_source = kilojoule / sec
                say("The energy exerted from your source in joules per second is:")
                print(energy_from_source, "/ second")
            else:
                say("Please type if joules to watts - 1 else: 2")
                turururururururuur = int(input())
                if turururururururuur == 1:
                    say("Please enter number of joules")
                    joules = int(input())
                    say("Please enter seconds")
                    seconds = int(input())
                    watts = joules / seconds
                    say("The answer to your question is")
                    print(watts)
                else:
                    say("Please enter number of watts:")
                    watts = input()
                    watts1 = int(watts)
                    print(watts, "is", watts1, "/second")
def matrix_time():
    say("Which city's time do you want if NY- 1 if London- 2 Dubai- 3 if qutar - 4 if Kentukky- 5")
    bytes = int(input())
    if bytes == 1:
        tz_NY = pytz.timezone("America/New_York")
        datetime_NY = datetime.now(tz_NY)
        a = datetime_NY.strftime("%H:%M:%S")
        print("New York's time is", a)
    elif bytes == 2:
        tz_LONDON = pytz.timezone("Europe/London")
        datetime_LONDON = datetime.now(tz_LONDON)
        a = datetime_LONDON.strftime("%H:%M:%S")
        print("London's time is", a)

    elif bytes == 3:
        tz_DUBAI = pytz.timezone("Asia/Dubai")
        datetime_Dubai = datetime.now(tz_DUBAI)
        a = datetime_Dubai.strftime("%H:%M:%S")
        print("Dubai's time is", a)

    elif bytes == 5:
        tz_KEN = pytz.timezone("America/Kentucky/Louisville")
        datetime_KEN = datetime.now(tz_KEN)
        a = datetime_KEN.strftime("%H:%M:%S")
        print ("Kentucky's time is", a)

    elif bytes == 4:
        tz_QUATAR = pytz.timezone("Asia/Qatar")
        datetime_QUATAR = datetime.now(tz_QUATAR)
        a = datetime_QUATAR.strftime("%H:%M:%S")
        print("Quatar's time is", a)
def matrix_hcf():
        say("Please enter two numbers")
        x = int(input())
        y = int(input())
        if x > y:
            smaller = x
        else:
            smaller = y
        for i in range(1, smaller + 1):
            if ((x % i == 0) and (y % i == 0)):
                hcf = i
        say("The HCF of the two numbers is")
        print("It is", hcf)
def main():
    matrix_access()
main()
