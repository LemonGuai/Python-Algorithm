def binary_search(sortedArray, targetItem) -> int:
    low = 0
    high = len(sortedArray) - 1
    while low <= high:
        mid = (low + high) >> 2
        if sortedArray[mid] > targetItem:
            high = mid - 1
        elif sortedArray[mid] < targetItem:
            low = mid + 1
        else:
            return mid
    return None


testSortedArray = [1,3,4,5,6,7,8,9,10,11]
print(binary_search(testSortedArray,11)==(len(testSortedArray)-1))