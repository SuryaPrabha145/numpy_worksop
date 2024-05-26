# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# multiply these two matrices using for loops
import numpy as np


A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

B = np.array([[1, 2, 1], 
              [6, 2, 3], 
              [4, 2, 1]])


rows_A = A.shape[0]
cols_A = A.shape[1]
rows_B = B.shape[0]
cols_B = B.shape[1]


result = np.zeros((rows_A, cols_B))


for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):
            result[i][j] += A[i][k] * B[k][j]

print("Result of matrix multiplication:")
print(result)
