# instertion sort is an in place comparison based osrting algortihm that places an unsorted element at its suitable place in each iteration

def insertionSort(arr):
    #start loop at the unsorted list. By default the first index or index 0 is sorted so we start at index 1
    for i in range(1, len(arr)):

        # We need to select our key first or the first element of our unsorted list so index + 1    or since our range starts at 1 it would be arr[i]
        key = arr[i]
        # we need the last element of our sorted list so it would be the the element right before our key or our key position - 1 
        lastElement = i - 1
        # while out last element is greater than 0 and our key is less that the last element loop
        while lastElement >= 0 and key < arr[lastElement]:
            # if condition above is true then swap the last element with the last element +1 or shift it right 1 index
            arr[lastElement + 1] = arr[lastElement]
            # must decrease last position to work down to 0 and eventually breack loop
            lastElement = lastElement -1 
        # when we are done comparing we swap our key with last + 1 since last + 1 is -1 we will insert at 0 index
        arr[lastElement + 1] =  key

arr = [29, 10, 14, 37, 14]
insertionSort(arr)

print(arr)
