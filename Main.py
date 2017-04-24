import math
from timeit import default_timer as timer

def factor(n):
    num = []
    # add 2 to list or prime factors and remove all even numbers(like sieve of ertosthenes)
    while (n % 2 == 0):
        num.append(2)
        n /= 2

    # divide by odd numbers and remove all of their multiples increment by 2 if no perfectlly devides add it
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            num.append(i)
            n /= i

    # if no is > 2 i.e no is a prime number that is only divisble by itself add it
    if n > 2:
        num.append(n)

    #print (num)

trials = 100
for i in range (0,trials):

    begin = timer()
    factor(1369592039)
    end = timer()
    executionTime = (end - begin)*1000000 #microseconds
    print(executionTime)

    