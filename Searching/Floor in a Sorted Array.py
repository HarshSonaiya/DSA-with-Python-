'''
Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is 
defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).

Example 1:
Input:
N = 7, x = 0 
arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less than 0 is found. So output is "-1".

Example 2:
Input:
N = 7, x = 5 
arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is 2 (i.e K = 2), whose index is 1(0-based indexing).

'''

def findFloor(self,A,N,X):
        low, high = 0, N - 1
        result = -1  # Initialize result to -1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] > X:    #If arr[mid] is greater than x
                high = mid - 1
            else:
                result = mid      #returning the index value
                low = mid + 1  #If arr[mid] is lesser than x

        return result
