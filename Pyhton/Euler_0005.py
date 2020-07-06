'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
'''


def compute():
    m = 1
    for n in range(1, 11):
        m *= n
    return m


if __name__ == '__main__':
    print(compute())
