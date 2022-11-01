# Divide and Conquer algorithm. It picks and element as a pivot and partitions the given array around the picker pivot. 

def quickSort(arr):
    pivotPoint(arr, 0, len(arr) -1 )
    return arr

def pivotPoint(arr, low, high):
    if low >= high:
        return
    #start our pivot at the beginning of the array.
    pivot = low
    #our left index to compare is index 0 + 1 
    left = low + 1
    # our right index is the ending value
    right = high
    # while out right index is greater than our left loop. 
    while right >= left:
        #compare value of our left index value is greater that value at pivot and the value of right is less that value of pivot 
        # if this is the case that means we need to switch the values so that lower are on left and higher on right. 
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left]
        # if our value at left index is less thatn or == to out pivot then we increment left pointer by 1 until we get to our pivor point 
        if arr[left] <= arr[pivot]:
            left += 1
        # if our value at our right index then we need to decrease our right index towards our pivot point
        if arr[right] >= arr[pivot]:
            right -= 1
    #if our pointers cross that means we need to swap our pivor with the right pointer
    arr[pivot], arr[right] = arr[right], arr[pivot]
    # we now have to arrays that we need to call out quicksort recursive function to sort them
    #left side array is our lowest left point and right -1 since we swapped our right index with our pivot
    pivotPoint(arr, low, right - 1)
    # left side is the opposite of above so right + 1 to end of arr
    pivotPoint(arr, right +1, high)

arr = [10, 3, 4, 5, 129, 400, 80]

quickSort(arr)

print(arr)