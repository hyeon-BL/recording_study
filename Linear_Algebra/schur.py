import numpy as np
from scipy.linalg import schur

# 예제 행렬 A
A = np.array([[4, -1],
              [1,  0]])

# Schur 분해
T, Q = schur(A)

print("상삼각 행렬 T:")
print(T)
print("\n유니타리(또는 직교) 행렬 Q:")
print(Q)
print("\n검증: Q @ T @ Q^H")
print(Q @ T @ Q.T)  # Q.T는 Q의 전치
