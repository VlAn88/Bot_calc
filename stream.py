import colorama
from datetime import timedelta, datetime

colorama.init()
from colorama import Fore, Back, Style
print (Fore.YELLOW + "Hello! I’ll help you find out the speed of visitor flow at the Russian Embassy in Yerevan!" + Style.RESET_ALL)
positions = [int(num) for num in input().split()]
def calculation(a): # calculation function
    diff = 0
    for item in range (len(a)-1):
        diff = diff + (a[item+1] - a[item])
    pace = -(diff/(item+1))
    nowDate = datetime.now()
    expire = timedelta(positions[-1]//pace)
    targetDate = nowDate + expire
    return print(Fore.GREEN + "The queue pace is ", round(pace, 1), "\n" "You will be received at the Embassy ", targetDate.strftime("%d %B %Y (%A)"))

if len(positions) <= 1:
    print(Fore.LIGHTMAGENTA_EX + "Not enough data. You need to enter at least two numbers")
    print (Fore.LIGHTMAGENTA_EX + "Do you want to enter more data?")
    print (Fore.LIGHTMAGENTA_EX + "Please, enter", Fore.LIGHTGREEN_EX + 'Yes', Fore.LIGHTMAGENTA_EX + "or", Fore.LIGHTRED_EX + 'No' + Style.RESET_ALL)
    answer = input()
    if answer == "No":
        print (Fore.GREEN + "Thank you for your attention. Contact me as soon as you have new data.")
    else:
        positions.extend(int(num) for num in input().split())
        print(positions)
        calculation (positions)
else:
    calculation (positions)
