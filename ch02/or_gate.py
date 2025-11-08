import numpy as np

from ch02.utils import visualize

# 가중치
w1 = 0.5
w2 = 0.5
# 편향
b = -0.2

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([w1, w2])

    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    visualize(w1, w2, b, OR)