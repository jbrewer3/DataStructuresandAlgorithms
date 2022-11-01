#The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm. In this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner.

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    #fget the middle point of our array to split in two
    middleElement =  len(arr) // 2
    #left array is from 0 to the middle element
    leftArr = arr[:middleElement]
    #rifght array is from middle to end
    rightArr = arr[middleElement:]
    # call recursive function to continue this until only 1 element exist for both left and right. 
    leftResult = mergeSort(leftArr)
    rightResult = mergeSort(rightArr)

    #merged the sorted list function call
    return merge(leftResult, rightResult)

#fuction to merge sorted list
def merge(leftResult, rightResult):

    sortedArray = [None] * (len(leftResult) + len(rightResult))
    #instantiate our pointers i pointing to first element in left result j will point to first element in right result k will point to first element in the sorted array
    
    i=j=k = 0
    # to keep pointer in the bounds of the list we loop while they are less than the len of the left and right results. 
    while i < len(leftResult) and j < len(rightResult):
        # if the left result value at i index is less that the right result at value of j then we will add the left result to the sorted array at index k 
        if leftResult[i] <= rightResult[j]:
            sortedArray[k] = leftResult[i]
            #increment index in left result and compare again
            i += 1
        # if the value of index j is less that value at index at i then put value of index j in sorted array
        else:
            sortedArray[k] = rightResult[j]
            #increment j to the next index 
            j += 1
        #increment k so that when we input another value it is at the next index. 
        k += 1
    # handles cases where we have no more values in j so if i is still in our left result then add all i index values to sorted list
    while i < len(leftResult):
        sortedArray[k] = leftResult[i]
        i += 1
        k += 1
    # if pointer is still in j right result the add all elements in right result to sorted array. 
    while j< len(rightResult):
        sortedArray[k] = rightResult[j]
        j += 1
        k += 1
    
    return sortedArray

arr = [12, 42, 1, 0, 50, 44, 99]

print(mergeSort(arr))

