import random

A = [ random.randint(1,6) for i in range(10) if i%2 == 0]
x = 1 if 2>3 else 5
f = lambda x:x**2

print(A, x, f(5))

def f():
    return 3 if 6>5 else 0

# min, max, sum, sorted, list, set, dict X one line for
