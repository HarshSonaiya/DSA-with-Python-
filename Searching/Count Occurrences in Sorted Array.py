'''
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(logn) 

Approach 1 : Use Binary Search 
'''

def search(nums, target, find_start_index):
    answer = -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            answer = mid
            if find_start_index:
                end = mid - 1
            else:
                start = mid + 1
    return answer

def count_occurrences(nums, x):
    first_index = search(nums, x, True)
    last_index = search(nums, x, False)
    if first_index != -1 and last_index != -1:
        return last_index - first_index + 1
    else:
        return 0
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
c = count_occurrences(arr, x)
print(c)
