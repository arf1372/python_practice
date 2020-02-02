# use square root (sqrt) from math library
from math import sqrt
def prime_factor(n):
    a_list = []
    # calculate all factors of entered number
    # use sqrt to reduce calculating
    for num in range(2, int(sqrt(n))):
        if n % num == 0:
            # assume all factors are prime
            is_prime = True
            # check factors for is prime or is not.
            for i in range(2, num // 4):
                if num % i == 0:
                    # because of this condition factors is not prime
                    # and this factor is not usefull then break loop
                    is_prime = False
                    break
            if is_prime:
                a_list.append(num)
    # print("prime factors of number {} is -->>".format(n), a_list)
    # if a_list = []  -->>  empty list
    # not a_list is Equal a_list = []
    if not a_list:
        # print("Number {} is prime, already.".format(n))
        pass
    else:
        return max(a_list)

if __name__ == '__main__':
    print(prime_factor(600851475143))
