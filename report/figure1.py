#!/usr/bin/env python

import matplotlib.pyplot as plt

points = [
    # alpha, accuracy
    [0.25, 0.505319],
    [0.5, 0.505788],
    [0.75, 0.508253],

    [0.3, 0.505906],
    [0.4, 0.506414],
    [0.6, 0.507275],
    [0.8, 0.508135],

    [0.9, 0.508018],
]

plt.scatter([p[0] for p in points], [p[1] for p in points])
plt.show()
