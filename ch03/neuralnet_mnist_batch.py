import numpy as np

from ch03.neuralnet_mnist import init_network, predict, get_data

x, t = get_data()
network = init_network()

batch_size = 100
acurracy = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i + batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    acurracy += np.sum(p == t[i:i + batch_size])

print(f"Accuracy: {acurracy / len(x)}")