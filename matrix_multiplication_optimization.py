import numpy as np
import time
import timeit

for k in range(1,12):
    """ Tests both (AB)X and A(BX) to test which is faster,
    Uses a for loop to do each calculation 100 times and divide by 100 to get mean,
    NOTE: Because it does 50 iterations to get a statistically accurate result,
    it does take a good ten to 50 seconds to run,
    prints results
    """
    A = np.ones((2**k,2**k))
    B = np.ones((2**k,2**k))
    X = np.ones((2**k,1))
    start_first = time.time()
    for j in range(0,50):
            C = A @ B
            D = C @ X
    elapsed_first = (time.time() - start_first) / 50
    start_second = time.time()
    for i in range(0,50):
            E = B @ X
            F = A @ E
    elapsed_second = (time.time() - start_second) / 50
    ratio = elapsed_first / elapsed_second
    print("This is for matrices of the size 2 to the ",k)
    print("TIme elspased for (AB)X : ",elapsed_first)
    print("Time elapsed for A(BX): ",elapsed_second)
    print("Ratio of the two: ",ratio)
    print('')


for n in range(1,12):
    """Tests computation times for different ways to multiply
    matrices and vectors.
    """
    size = 2**n
    G = np.eye(size)
    U = np.ones((size,size))
    V = np.ones((size,size))
    X = np.ones((size,1))
    start_first = time.time()
    for j in range(0,50):
            H = U @ V.T
            I = H + G
            J = I @ X
    elapsed_first = (time.time() - start_first) / 50
    start_second = time.time()
    for i in range(0,50):
            K = V.T @ X
            L = U @ K
            M = X + L
    elapsed_second = (time.time() - start_second) / 50
    ratio = elapsed_first / elapsed_second
    print("This is for matrices of the size 2 to the ",n)
    print("TIme elspased for (AB)X : ",elapsed_first)
    print("Time elapsed for A(BX): ",elapsed_second)
    print("Ratio of the two: ",ratio)
    print('')
