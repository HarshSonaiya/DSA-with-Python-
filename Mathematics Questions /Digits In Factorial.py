'''
Given an integer N. Find the number of digits that appear in its factorial. 
Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.

Approach 1 : T(n) = O(n)
Calculate factorial(N) and store it in variable 'fact'.
Count number of digits present in 'fact'by initializing variable 'd' with 0, 
to store number of digits in 'fact'.
while 'fact' is not equal to 0, increase 'd' by 1 and divide 'fact' by 10.
Return 'd' as answer.
'''

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def digits_in_factorial(N):
    # finding factorial of a number
    fact = factorial(N)

    # counting the number of digits present
    # in the factorial of number N
    d = 0
    while fact != 0:
        fact //= 10
        d += 1
    return d
'''
Approach 2 : T(n) = O(n)

The idea is to make use of properties of log:
Property 1:-
For a number X, number of digits in X will be (floor(log(X)) + 1). 

Proof:
Let x be a positive integer with k digits. This means that:
10^(k-1) <= x < 10^k
Taking logarithms base 10 of both sides, we get:
k-1 <= log(x) < k
Adding 1 to both sides, we get:
k <= log(x) + 1 < k+1
Taking the floor of both sides, we get:
k = floor(log(x) + 1)
Therefore, the number of digits in x is equal to floor(log(x) + 1).

Property 2 :-
log(X * Y) = log(X) + log(Y). 
So number of digits in N! will be:
=>  floor(log(N!)) + 1
=> floor(log(1*2*3...*N)) + 1
=> floor(log(1)+log(2)+log(3)...+log(N)) + 1.
Note: log used here is having base of 10.

Implementation
Initialize a variable 'sum' of type double with 0.
Run a loop for j from 1 to N:
Add log10(j) to the sum.
Return (1+ floor(sum)) as answer.
Let us understand it better with the help of an example:
Input: N = 5
log1 = 0
log2 = 0.30103
log3 = 0.477121
log4 = 0.60206
log5 = 0.69897
log(5!) = (log1+log2+log3+log4+log5) = 2.07918
So the number of digits in 5! is (1 + floor(2.07918)) which is 3.
'''

def digitsInFactorial(self,N):
        if(N==1):
            return 1
        
        if(N==0) :
            return 0# code here
        import math 
        count=0
        fact =1 
        for i in range(2,N+1):
            count += math.log10(i)
        
        return math.floor(count)+1
