"""
Create a function that takes an integer as an argument and returns True if it’s a prime number, and False otherwise.

"""

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n%i==0:
            return False
    return True
n = int(input("Enter the Number:"))
print(f"{n} is prime:",is_prime(n))


print("#"*100)

"""
Using the function defined in the previous challenge, find and return five prime numbers greater than 1,000,000.
"""


def five_primes_after_million():
    primes=[]
    num=1000001

    while len(primes)<5:
        primes.append(num)
        num+=1
    return primes
print("First five primes greater than 1,000,000 are:")
print(five_primes_after_million())


