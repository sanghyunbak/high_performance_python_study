# find prime number
import math

from termcolor import colored
# import colored as colored


def check_prime(number):
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False
    return True


if __name__ == '__main__':
    print(colored(f'check_prime(10,000,000): {check_prime(10_000_000)}', 'green'))
    print(colored(f'check_prime(10,000,019): {check_prime(10_000_019)}', 'green'))
