'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(n):
    digits = str(n)
    if len(digits) % 2 == 0:
        middle = int(len(digits)/2)
        second_half = digits[:middle-1:-1]
    else:
        middle = int((len(digits)-1)/2)
        second_half = digits[:middle:-1]
    first_half = digits[:middle]
    if first_half == second_half:
        return True
    else:
        return False


def compute():
    last_palindrom = 0
    for x in range(999, 99, -1):
        for y in range(999, 99, -1):
            res = x * y
            if is_palindrome(res):
                if res > last_palindrom:
                    last_palindrom = res
                else:
                    break
    return last_palindrom


if __name__ == '__main__':
    print(compute())
