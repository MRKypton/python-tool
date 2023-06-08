import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(arg):
    result = [random.randint(30, 40), random.randint(30, 40)]
    result.append(arg - sum(result))
    
    while not (12 <= result[2] <= 20):
        result = [random.randint(30, 40), random.randint(30, 40)]
        result.append(arg - sum(result))
    
    print(result)

clear_console()

while True:
    arg = int(input("What number do you want me to generate: "))
    if 70 < arg < 100:
        main(arg)
        input("\nPress Enter to continue...")
    else:
        print("Error: Your number must be in the range of 71 - 99")
        input("\nPress Enter to continue...")
    clear_console()
