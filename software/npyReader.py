import sys
import numpy as np
L = np.load(sys.argv[1], allow_pickle=True)
print("\nshape={}\n".format(L.shape))
if len(L.shape)==1:
    if len(L)<=200:
        for i in range(200):
            print(L[i], end=" ")
    else:
        for i in range(100):
            print(L[i], end=" ")
        print("\n...\n...\n...\n")
        for i in range(100):
            print(L[i], end=" ")
else:
    print(L)
print("\n")
