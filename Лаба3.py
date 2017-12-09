from math import sqrt
import numpy as np

ITERATION_LIMIT = 30

# initialize the matrix
A = np.array([[0.563 , -0.2 , 0.1] ,
              [-0.1 , 0.4988 , -0.1] ,
              [-0.2988 , 0.2 , -0.488]])
b = np.array([0.4093 , 0.7801 , -1.3619])
eps=0.5*10**(-4)

def seidel(A, b, eps):
    n = len(A)
    x = [.0 for i in range(n)]
    count=0
    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
            count+=1
        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new
    return print('Решение по методу Зейделя: '+str(x)+str(count))
def jacobi(A,b,ITERATION_LIMIT):
    count = 0
    x = np.zeros_like(b)
    for it_count in range(ITERATION_LIMIT):
        print("Решение на шаге:" , x)
        x_new = np.zeros_like(x)
        count+=1
        for i in range(A.shape[0]):
            s1 = np.dot(A[i , :i] , x[:i])
            s2 = np.dot(A[i , i + 1:] , x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i , i]
        x = x_new
    print()
    print("Решение по методу Якоби :" +str(x)+''+str(count))
    
jacobi(A,b,ITERATION_LIMIT)
seidel(A, b, eps)
