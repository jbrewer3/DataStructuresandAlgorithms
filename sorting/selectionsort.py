# Selection sort is an algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list. 

def selectionSort(arr):
    for i in range(len(arr)):
        #for each iteration get the minimum indexed value sets the item to compare
        min_x = i
        # for each iteration we can start at the nex index so i+1 for the len of our range to the max of our range. range increased with each iteration
        for x in range(i+1, len(arr)):
            #if the index at arr[x] <  the current smallest index then make the new minimum value at arr[x]
            if arr[x] < arr[min_x]:
                min_x = x        
        #after comparing all values we swap the minimam with the index we are comparing
        arr[i], arr[min_x] = arr[min_x], arr[i]       

arr = [20, 12, 10, 15, 2]

selectionSort(arr)

print(arr)
    