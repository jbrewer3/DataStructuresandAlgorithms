

def binarySearch(arr, target):
    left = 0
    right = len(arr) -1
    #helper function does recursion task
    result = helper(arr, target, left, right)
    return result

def helper(arr, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    middle_element = arr[middle]

    if target == middle_element:
        return middle
    elif target < middle_element:
        right = middle -1
        return helper(arr, target, left, right)
    else:
        left = middle +1
        return helper(arr, target, left, right)