#!/usr/bin/env python

import matplotlib.pyplot as plt

points = [
    # alpha, accuracy
    [1, 1.54],
    [2, 1.198],
    [3, 2.917],
    [10, 27.955],
    [20, 105],
]

badpoints = [
    # alpha, accuracy
    [2, 2.407],
    [3, 3.094],
    [10, 43.126],
    [20, 217],
]

plt.scatter([p[0] for p in points], [p[1] for p in points], c='b')
plt.scatter([p[0] for p in badpoints], [p[1] for p in badpoints], c='r')
plt.show()
