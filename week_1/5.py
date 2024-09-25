import math
a = [8, 9, 10, 11, 13, 81, 101, 100, 94]

def prime_check(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

for num in a:
    is_prime = prime_check(num)
    if is_prime:
        print(f"{num} is prime: {is_prime} and square of {num} is {num**2}")