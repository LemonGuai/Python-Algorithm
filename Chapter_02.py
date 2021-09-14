'''
选择排序-refs:算法图解P25
'''
def findmin(arrayToSort):
    min = arrayToSort[0]
    minIndex = 0
    for i in range(len(arrayToSort)):
        if arrayToSort[i] < min:
            min = arrayToSort[i]
            minIndex = i

    return minIndex

# 时间复杂度 o(n^2)
def selectionSort(arrayToSort):
    sortedArray = []
    for i in range(len(arrayToSort)):
        min = findmin(arrayToSort)
        sortedArray.append(arrayToSort.pop(min))
    return sortedArray


print(selectionSort([5,3,6,2,10]))

