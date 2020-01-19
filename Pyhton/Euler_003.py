'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from sympy.ntheory import isprime

number = 600851475143


def compute(n):
    res = 1
    for i in range(2, n):
        if isprime(i) and n % i == 0:
            res *= i
            if res == n:
                return i


if __name__ == '__main__':
    print(compute(number))
