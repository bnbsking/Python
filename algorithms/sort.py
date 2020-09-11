from random import randint as rd

def quickSort(l=0,r=len(L)-1):
    if l<r:
        pivot, i, j = L[l], l+1, r
        while i<j:
            while L[i]<=pivot and i<j: # <=避免[1,1,1]會無窮迴圈
                i+=1
            while L[j]>=pivot and i<j:
                j-=1
            L[i], L[j] = L[j], L[i]
        L[l], L[i] = min(L[l], L[i]), max(L[l], L[i]) # i-1前<pivot i+1後>pivot
        quickSort(l,i-1)
        quickSort(i,r)

for i in range(100):
    L = [ rd(-100,100) for i in range(rd(0,100)) ]
    M = L[:]
    M.sort()
    print(M.sort()==L.sort(), end=' ')
