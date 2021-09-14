'''
二分算法-refs:图解算法page7
'''
def binary_search(sortedArray, targetItem) -> int:
    low = 0
    high = len(sortedArray) - 1
    while low <= high:                          #只要查找范围在两个元素及以上
        mid = (low + high) >> 2
        guess = sortedArray[mid]
        if guess == targetItem:
            return mid
        elif guess > targetItem:
            high = mid - 1
        else :
            low = mid + 1
    return None


testSortedArray = [1,3,5,7,9]
print(binary_search(testSortedArray,-1)==None)