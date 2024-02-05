// Prime numbers are those that are divisible only by 1 and themselves.
// Given a number N, check if it is prime or not.

// Python Code:

// Approach 1: Brute Force Method (Time Complexity T(n) = O(n))

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

// Approach 2: Time Complexity T(n) = O(sqrt(n))
// Divisors always occur in pairs. For example, check if 10 is prime or not.
// Factors of 10 are 1, 2, 5, 10 --> 1 x 10 = 10, 2 x 5 = 10, 5 x 2 = 10, 10 x 1 = 10
// So if (x, y) is a pair of factors like (2, 5) and x is less than or equal to y,
// then the following is always true for (x, y): x * x < n (because x is less than y)

def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

// Approach 3: Optimized Approach T(n) = O(sqrt(n))
// Every prime number (P) can be expressed in the form "6K + 1" or "6K - 1".
// Thus, check if P is prime by dividing from 2 to sqrt(n) but skipping multiples of 6
// because if all other numbers except multiples of 6 cannot divide the number P,
// it means it can be expressed in the form "6K + 1" or "6K - 1". Hence, it is a prime number.

import math

def isPrime(N):
    if N <= 1:
        return False
    if N == 2 or N == 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(N)) + 1, 6):  // Increment i by 6 to avoid checking with factors of 6
        if N % i == 0 or N % (i + 2) == 0:
            return False
    return True
