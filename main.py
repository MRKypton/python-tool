import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(arg):
    result = [random.randint(30, 40), random.randint(30, 40)]
    max_val = min(arg - sum(result), 20)

    if max_val >= 12:
        result.append(random.randint(12, max_val))
    else:
        result.append(12)

    while not (12 <= result[2] <= 20):
        result = [random.randint(30, 40), random.randint(30, 40)]
        max_val = min(arg - sum(result), 20)

        if max_val >= 12:
            result.append(random.randint(12, max_val))
        else:
            result.append(12)

    print(result)

clear_console()

while True:
    try:
        arg = int(input("What number do you want me to generate: "))
        if 70 < arg < 100:
            main(arg)
            input("\nPress Enter to continue...")
        else:
            print("Error: Your number must be in the range of 71 - 99")
            input("\nPress Enter to continue...")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        input("\nPress Enter to continue...")
    clear_console()
