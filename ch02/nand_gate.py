import numpy as np
from ch02.utils import visualize

# 가중치
w1 = -0.5
w2 = -0.5
# 편향
b = 0.7

# 목적: AND 퍼셉트론을 조건을 반대로 → AND 퍼셉트론의 w, b를 0을 기준으로 반대값으로 변경(양수는 음수로, 음수는 양수로)
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([w1, w2])

    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    visualize(w1, w2, b, NAND)