A = [2,4,6,8]

def binarySearchInsert(A,target):
    l, r = 0, len(A)-1
    while l<=r:
        m = (l+r)//2
        if A[m]>target:
            r = m-1
        elif A[m]==target:
            l, r = m, m-1
        else:
            l = m+1
    return l

for i in range(0,10):
    print(i, binarySearchInsert(A,i))
"""
0 0
1 0
2 0
3 1
4 1
5 2
6 2
7 3
8 3
9 4
"""