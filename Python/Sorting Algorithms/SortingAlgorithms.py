import Framework
from BubbleSort import BubbleSort
from SelectionSort import SelectionSort


LENGTH = 1000
ITERATIONS = 10
    
def main():
    selection_times = []
    bubble_times = []
    arr = Framework.GenerateRandomArray(LENGTH)
    for x in range(0,ITERATIONS):
        selection_times.append(Framework.RunAlgorithm(SelectionSort, arr.copy()))
        bubble_times.append(Framework.RunAlgorithm(BubbleSort, arr.copy()))
    print("Average time for Selection Sort: %d ns" % int(sum(selection_times) / len(selection_times)))
    print("Average time for Bubble Sort: %d ns" % int(sum(bubble_times) / len(bubble_times)))


if __name__ == "__main__":
    main()