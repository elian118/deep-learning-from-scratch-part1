import numpy as np
from ch02.utils import visualize

# 가중치
w1 = 0.5
w2 = 0.5
# 편향
b = -0.7 # AND 퍼셉트론의 목적을 달성하려면 b(편향) 값은 -1.0 < b < -0.5 범위 내에 아무 숫자나 설정해주면 된다.

# 목적: 뉴런에서 보내온 신호의 총 합이 정해진 한계를 넘어설 때만 1을 출력
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([w1, w2])

    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    visualize(w1, w2, b, AND)