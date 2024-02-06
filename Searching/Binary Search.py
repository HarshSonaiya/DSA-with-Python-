'''
Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

Binary Search Algorithm: The basic steps to perform Binary Search are:

1. Begin with the mid element of the whole array as search key.
2. If the value of the search key is equal to the item then return index of the search key.
3. Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
4. Otherwise, narrow it to the upper half.
5. Repeatedly check from the second point until the value is found or the interval is empty.

Recursive implementation of Binary Search:
'''

  def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")

" Iterative implementation of Binary Search:" 

  def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")

'''
Note: Here we are using:  **** int mid = low + (high – low)/2;   ****
instead of int mid = (low + high)/2; because if we calculate the middle index 
like this means our code is not 100% correct, it contains bugs.
That is, it fails for larger values of int variables low and high. 
Specifically, it fails if the sum of low and high is greater than the maximum positive int value(2^31 – 1 ).
The sum overflows to a negative value and the value stays negative when divided by 2. 
'''
