'''
递归, Method Name Suffix = StandardAnswer表示为《算法图解》提供的参考答案
'''


# 4.1 实现数组sum()
def sumArray(arrayToSum):
    if len(arrayToSum) <= 1:
        return arrayToSum.pop()
    else:
        return arrayToSum.pop() + sumArray(arrayToSum)


def sumArrayStandardAnswer(list):
    if list == []:
        return 0
    else:
        return list[0] + sumArrayStandardAnswer(list[1:])

print(sumArray([12,5,43,4]))

# 4.2 实现数组count()
def countArray(arrayToCount):
    if len(arrayToCount) <= 1:
        return 1
    else:
        arrayToCount.pop()
        return 1 + countArray(arrayToCount)


def countArrayStandardAnswer(list):
    if list == []:
        return 0
    else:
        return 1 + countArrayStandardAnswer(list[1:])

print(countArray[1,5,2,6,34])

# 4.3 实现数组max(), 先抛出一个item,用这个item去跟剩余list中的max比较, 大的则为max
def findMax(arrayToFindMax):
    if len(arrayToFindMax) <= 1:
        return arrayToFindMax.pop()
    else:
        maxItem = arrayToFindMax.pop()
        nextItem = findMax(arrayToFindMax)
        if maxItem >= nextItem:
            return maxItem
        else:
            return nextItem


def findMaxStandardAnswer(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = findMaxStandardAnswer(list[1:])
        return list[0] if list[0] > sub_max else sub_max

print(findMaxStandardAnswer([1,2,8,23,5,8]))

# 4.4 二分查找,返回索引 ***************************************很重要
def binary_search(sortedList, targetItem) -> int:
    return getNewSortedList(sortedList, 0, len(sortedList) - 1, targetItem)


def getNewSortedList(sortedList, low, high, targetItem):
    if low <= high:
        mid_index = (low + high) >> 1
        mid = sortedList[mid_index]
        if mid == targetItem:
            return (low + high) >> 1
        elif mid > targetItem:
            mid_index -= 1
            return getNewSortedList(sortedList, low, mid_index, targetItem)
        else:
            mid_index += 1
            return getNewSortedList(sortedList, mid_index, high, targetItem)
    else:
        return None

print(binary_search([1,4,5,8,6],8))
print(binary_search([1,4,5,8,6],7))

# 快速排序
def quickSort(list) -> list:
    if len(list) < 2:
        return list
    else:
        flagItem = list[0]
        less = [item for item in list[1:] if item <= flagItem]
        greater = [item for item in list[1:] if item > flagItem]
        return quickSort(less) + [flagItem] + quickSort(greater)


print(quickSort([6,5,4,1, 3, 5, 7, 9]))
