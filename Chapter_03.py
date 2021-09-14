'''
递归-refs:算法图解P32
'''
def countDown(i):
    print(i)
    if i<=1:                # base case:基线条件
        return
    else:                   # recursive case: 递归条件  
        countDown(i-1)


countDown(10)