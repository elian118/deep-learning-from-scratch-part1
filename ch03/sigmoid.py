import numpy as np
from matplotlib import pyplot as plt


# 입력 배열을 0~1 사이 값으로 비례 조정
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

if __name__ == "__main__":
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()