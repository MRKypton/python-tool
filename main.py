import random

def main(*args):
    results = []
    
    for arg in args:
        result = [random.randint(30, 40), random.randint(30, 40)]
        result.append(arg - (result[0] + result[1]))
        
        while result[2] < 12 or result[2] > 20:
            result = [random.randint(30, 40), random.randint(30, 40)]
            result.append(arg - (result[0] + result[1]))
        
        results.append(result)
    
    return results

print(main(90,80,75))