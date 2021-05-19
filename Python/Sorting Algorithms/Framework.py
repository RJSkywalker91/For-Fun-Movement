import random
import time

def SwapElements(x, y, arr):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def GenerateRandomArray(len):
    arr = [*range(0,len)]
    random.shuffle(arr)
    return arr

def RunAlgorithm(func, arr):
    start = time.perf_counter_ns()
    func(arr)
    end = time.perf_counter_ns()
    return int(end - start)