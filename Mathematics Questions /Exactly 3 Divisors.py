'''
Given a positive integer value N. The task is to find how many numbers less than 
or equal to N have numbers of divisors exactly equal to 3.

Brute force Approach : T(n) = O(N*N)

Run a for loop from 1 to N and then for each number x we can find the number of 
factors and if the number of factors is 3 then we will add 1 to our answer.
'''

def hasThreeDivisors(n):
    number_of_factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            number_of_factors += 1
    return number_of_factors == 3

def exactly3Divisors(N):
    ans = 0
    for i in range(1, N + 1):
        if hasThreeDivisors(i):
            ans += 1
    return ans
'''  
Optimized Brute Force: T(n) = O(n**1.5)

run a for loop from 1 to N and then for each number x we can find the number of factors 
and if the number of factors is 3 then we will add 1 to our answer. But this time we will
use the sqrt(N) approach to find the number of factors.
'''

def hasThreeDivisors(n):
    number_of_factors = 2
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            number_of_factors += 1
            if i * i != n:
                number_of_factors += 1
    return number_of_factors == 3

def exactly3Divisors(N):
    ans = 0
    for i in range(1, N + 1):
        if hasThreeDivisors(i):
            ans += 1
    return ans
'''
Optimized Solution : 

We can optimize the above solution by simple observation. The observation is only perfect squares
of primes can have exactly three divisors. So we need to find all primes p such that p*p<=N. 

Implementation:
Run a for loop from 1 to sqrt(N).
For each i determine if i is prime or not if i is prime then increment the answer.
To find if i is prime or not use the sqrt(N) approach as discussed here.
Return the answer.
'''

import math
def is_prime(self, n):
        if n == 1:
            return False
        for i in range(2, 1 + int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True

    def exactly_3_divisors(self, N):
        N_sqrt = int(math.sqrt(N))
        counter = 0
        for i in range(1, N_sqrt + 1):
            if self.is_prime(i):
                counter += 1

Time Complexity: O(N1/2 * N1/4) as we are running two nested for loops one from 1 to sqrt(N) and the other from 1 to sqrt(sqrt(N)).
