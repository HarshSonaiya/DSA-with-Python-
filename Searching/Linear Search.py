'''
Time Complexity : O(n)
Auxiliary Space: O(1)

A simple approach 

1. Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
2. If x matches with an element, return the index.
3. If x doesn’t match with any of elements, return -1.
'''
def search(arr, n, x):
    for i in range(0, n):
      if (arr[i] == x):
        return i
	return -1

arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else :
    print("Element is present at index", result)

'''
Improved Linear Search Worst-Case Complexity

if element Found at last O(n) to O(1) . It is the same as previous method because here we are 
performing 2 ‘if’ operations in one iteration of the loop and in previous method we performed only 1 ‘if’ operation.
This makes both the time complexities same.
'''
def search(arr, search_Element):
    left = 0
    length = len(arr)
    position = -1
    right = length - 1

    # Run loop from 0 to right
    for left in range(0, right, 1):
      #If search_element is found with
      # left variable
      if (arr[left] == search_Element):
          position = left
          print("Element found in Array at ", position +
              1, " Position with ", left + 1, " Attempt")
          break
      # If search_element is found with# right variable
      if (arr[right] == search_Element):
          position = right
          print("Element found in Array at ", position + 1,
              " Position with ", length - right, " Attempt")
          break
      left += 1
      right -= 1

    if (position == -1):        # If element not found
       print("Not found in Array with ", left, " Attempt")

arr = [1, 2, 3, 4, 5]
search_element = 5
search(arr, search_element)
