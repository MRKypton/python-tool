import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(*args)->void:
    results = []
    
    for arg in args:
        result = [random.randint(30, 40), random.randint(30, 40)]
        result.append(arg - (result[0] + result[1]))
        
        while result[2] < 12 or result[2] > 20:
            result = [random.randint(30, 40), random.randint(30, 40)]
            result.append(arg - (result[0] + result[1]))
        
        results.append(result)
        print(result)

clear_console()

while True:
    arg = int(input("What number do you want me to generate: "))
    if(70<arg<100):
        main(arg)
        input("\nPress Enter to continue...")
    else:
        print("Error : Your number must in range 71 - 99")
        input("\nPress Enter to continue...")
    clear_console()
