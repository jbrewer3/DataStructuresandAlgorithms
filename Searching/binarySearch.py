#can only be used if array is sorted. 

#set left and right pointers 
def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
# while the right pointer is greater that the left loop
    while left <= right:
        #set out starting point in the middle of the array. 0 + the length of the array floor divied by 2
        middle = (left + right ) // 2
        #get the middle element index
        middle_element = arr[middle]
        # if our target is  = to our middle element return middle
        if target == middle_element:
            return middle
        # if the target is less than the middle element eliminate the right half of the array by making our new right pointer our old middle
        elif target < middle_element:
            right = middle -1 
        # if the target is greater than the middle element eliminate the left half of the array by making our new left pointer our old middle
        else:
            left = middle + 1
print(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13], 5))