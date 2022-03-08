A = [1,2,3]
B = A             # call by reference
C = A[:]          # call by value
print(hex(id(A)), hex(id(B)), hex(id(C)))

A[0] = 100
print(A, B, C)

A = [i*i for i in range(100000)]
import time, copy

start = time.time()
B = A                 # assign pointer O(1)
finish = time.time()
print(finish-start)

start = time.time()
C = A[:]              # deep copy O(n) ? YES
finish = time.time()
print(finish-start)

start = time.time()
D = [i for i in A]  # deep copy O(n)
finish = time.time()
print(finish-start)

start = time.time()
E = copy.deepcopy(A) # deep copy O(n)
finish = time.time()
print(finish-start)
