import numpy as np

A = np.array([1,2,3,4])
B = np.array([[1,2],[3, 4], [5, 6]])

print(A)
print(f"A 차원 수: {np.ndim(A)}")
print(f"A 모양: {A.shape}")
print(f"A[0] 모양: {A.shape[0]}")
print('=' * 55)
print(B)
print(f"B 차원 수: {np.ndim(B)}")
print(f"B 모양: {B.shape}")
print(f"B[0] 모양: {B.shape[0]}")