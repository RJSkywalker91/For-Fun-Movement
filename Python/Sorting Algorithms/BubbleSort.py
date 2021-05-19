from Framework import SwapElements

def BubbleSort(arr):
    no_swaps = False
    while no_swaps == False:
        swap_occurred = False
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                SwapElements(i-1, i, arr)
                swap_occurred = True
        if swap_occurred == False:
            no_swaps = True