# Problem 1
import numpy as np
print("Problem 1:")
arr1 = np.array([i for i in range(1, 101)])
arr2 = arr1.reshape(10, 10)
print(arr1)
print(arr2)
print()

# Problem 2
print("Problem 2:")
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])
C = np.zeros((A.shape[0], B.shape[1]))

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            C[i, j] += A[i, k] * B[k, j]

print(C)
print()

# Problem 3
print("Problem 3:")
x = np.array([1, 2, 3, 4])
y = np.array([10])
result = x * y

print(result)
print()

# Problem 4 
print("Problem 4:")
matrix = np.random.normal(0, 1, (5, 5))
print(matrix)
print()

# Problem 5
print("Problem 5:")
Z = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
subarray = Z[:2, -2:]
print(subarray)
print()

# Problem 6
print("Problem 6:")
arr = np.random.rand(6, 4)
print(arr.reshape(6, 4, 1))
print()

# Problem 7
print("Problem 7:")
A = np.array([[1, 2], [3, 4]])
B = np.transpose(A)
print(np.dot(A, B))
print()

# Problem 8
print("Problem 8:")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

concatenated_array = np.concatenate((a, b))
print(concatenated_array)
print()

# Problem 9
print("Problem 9:")
v = np.array([12, 3, 10, 5, 8, 15, 7, 2])
a = v > 5 
filtered_v = v[a]
print(filtered_v)
print()

# Problem 10
print("Problem 10:")
M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

mean_rows = np.mean(M, axis=1)
mean_columns = np.mean(M, axis=0)

print("mean_rows:", mean_rows) 
print("mean_columns:", mean_columns)
