'''
Given a binary sorted non-increasing array of 1s and 0s. You need to print the count of 1s in the binary array.
Input:
N = 8
arr[] = {1,1,1,1,1,0,0,0}
Output: 5
Explanation: Number of 1's in given 
binary array : 1 1 1 1 1 0 0 0 is 5.
'''

def countOnes(self,arr,N):
        low=0
        high=N-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>1:
                low=mid+1
            elif arr[mid]<1:
                high=mid-1
            else:
                if mid==N-1 or arr[mid+1]!=1:
                    return mid+1
                else:
                    low=mid+1
        return 0
