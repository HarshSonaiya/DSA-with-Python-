// Given a positive integer N. The task is to find factorial of N.

def factorial(N):
        result = 1
        for i in range(2,N+1):
            result = result*i
        return result
