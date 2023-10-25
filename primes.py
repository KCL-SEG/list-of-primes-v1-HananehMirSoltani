"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def is_prime (number):
    if number<=1:
        return False
    elif number %2 == 0:
        return False
    else:
        for i in range (3, int(number/2)+1):
            if number%1==0:
                return False
            else:
                return True
    

def primes(number_of_primes):
    list = []
    num= 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
            num +=1
    return list



