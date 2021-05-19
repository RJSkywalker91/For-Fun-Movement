from Framework import SwapElements

def SelectionSort(arr):
    for current_index in range(0, len(arr)):
        min_index = current_index
        min_value = arr[current_index]
        for x in range(current_index + 1, len(arr)):
            if arr[x] < min_value:
                min_value = arr[x]
                min_index = x
        SwapElements(current_index, min_index, arr)