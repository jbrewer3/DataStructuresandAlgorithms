"""
bubble sort is based on the idea of repeatedly comparing pairs of adjacent element
and then swapping their positions if they exist in the wrong order. 
"""


def bubblesort(arr):
    # we must run iterate through this for every element in the array
    for iter in range(len(arr)):
        #for each index in the array we compare if left index is greater than right index and if so swap them .
        # we also decrement out range to leave out the already sorted items by subtracting the amount of iterations. 
        for index in range(0, len(arr) - 1 - iter):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]


arr = [29, 10, 14, 37, 14]
bubblesort(arr)


print(arr)