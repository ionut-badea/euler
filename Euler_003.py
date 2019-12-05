'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


import math


def compute():
    result = 0
    maxim = 13195
    half = math.ceil(maxim / 2)
    for n in range(1, half):
        if maxim % n == 0:
            result = n
    return result


if __name__ == '__main__':
    print(compute())
