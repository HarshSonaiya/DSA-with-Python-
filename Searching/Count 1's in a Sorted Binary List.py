'''
Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1's in it. 

Approach 1 : Time complexity: O(Log(N)) Auxiliary Space: O(log(N))

We can use Binary Search to find count in O(Logn) time. The idea is to look for the last occurrence of 1 using Binary Search. 
Once we find the index's last occurrence, we return index + 1 as count.

Follow the steps below to implement the above idea:

Do while low <= high:
Calculate mid using low + (high - low) / 2.
Check if the element at mid index is the last 1
If the element is not last 1, move the low to right side recursively and return the result received from it.
Otherwise, move the low to left recursively and return the result received from it.
The following is the implementation of the above idea. 
'''

def countOnes(arr, low, high):

    if high >= low:

        # get the middle index
        mid = low + (high-low)//2

        # check if the element at middle index is last 1
        if ((mid == high or arr[mid+1] == 0) and (arr[mid] == 1)):
            return mid+1

        # If element is not last 1, recur for right side
        if arr[mid] == 1:
            return countOnes(arr, (mid+1), high)

        # else recur for left side
        return countOnes(arr, low, mid-1)

    return 0

arr = [1, 1, 1, 1, 0, 0, 0]
print("Count of 1's in given array is", countOnes(arr, 0, len(arr)-1))
'''
Output
Count of 1's in given array is 4

Approach 2 : Time complexity: O(Log(N)) Auxiliary Space: O(1)

Count 1's in a sorted binary array using binary search iteratively:
Follow the steps below for the implementation:

Do while low <= high
Calculate the middle index say mid
Check if arr[mid] is less than 1 then move the high to left side (i.e, hight = mid - 1)
If the element is not last 1 then move the low to the right side (i.e, low = mid + 1)
Check if the element at the middle index is last 1 then return mid + 1
Otherwise move to low to right (i.e, low = mid + 1)
Below is the implementation of the above approach:
'''

def countOnes(arr, n):
    low = 0
    high = n - 1
    while (low <= high):  # get the middle index
        mid = (low + high) // 2

        # check if the element at middle index is last 1
        if ((mid == n - 1 or arr[mid + 1] == 0) and arr[mid] == 1):
            return mid + 1

        # check for 1 on left side
        if (arr[mid] == 0):
            high = mid - 1

        # check for 1 on right side
        elif(arr[mid] == 1):
            low = mid + 1

    return 0

arr = [1, 1, 1, 1, 0, 0, 0]
n = len(arr)

print("Count of 1's in given array is ", countOnes(arr, n))
'''
Output
Count of 1's in given array is 4
'''
