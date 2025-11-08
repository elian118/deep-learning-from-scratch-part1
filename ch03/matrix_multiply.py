import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A.shape)
print(B.shape)
print(np.dot(A, B)) # 수학적 행렬곱

print('='* 55)

C = np.array([[1, 2, 3], [4, 5, 6]])
D = np.array([[1, 2], [3, 4], [5, 6]])

print(C.shape)
print(D.shape)
print(np.dot(C, D)) # 수학적 행렬곱 # broadcast

print('='* 55)

E = np.array([[1, 2], [3, 4]])

print(C.shape)
print(E.shape)
print(np.dot(C, E)) # 수학적 행렬곱 # 오류 → 두 행렬의 대응하는 차원의 원소 수 불일치