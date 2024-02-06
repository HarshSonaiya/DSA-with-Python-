'''
An element is called a peak element if its value is not smaller than the value of its adjacent 
elements(if they exists). Given an array arr[] of size N, Return the index of any one of its peak elements. 
Expectime T(n) = O(log n)

Input: 
N = 3
arr[] = {1,2,3}
Possible Answer: 2
Explanation: index 2 is 3. It is the peak element as it is greater than its neighbour 2

N = 3
arr[] = {3,4,2}
Output: 1
Explanation: 4 (at index 1) is the peak element as it is greater than it's neighbor elements 3 and 2.
'''
def peakElement(self,arr, n):
        # Code here
        l = 0
        r = n-1
        if n==2:
            return 1 if arr[1]>arr[0] else 0
        while l<=r:
            m = l+(r-l)//2
            if m==0:
                return 0
            if m==n-1:
                return n-1
            if arr[m]>=arr[m+1] and arr[m]>=arr[m-1]:
                return m
            elif arr[m]>=arr[m+1] and arr[m]<=arr[m-1]:
                r = m
            else:
                l = m+1
