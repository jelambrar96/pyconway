
# python libraries
from typing import Tuple


# dependences
from scipy.signal import convolve2d
import numpy as np


class ConwayBoard:

    _kernel = np.array([1, 1, 1], [1, 0, 1], [1, 1, 1])

    def __init__(self, size):
        self.size = size
        self.state  = np.zeros(size, dtype=bool)

    def clear(self):
        self.state = np.zeros(self.size, dtype=bool)

    def __next(self):
        conv_result = convolve2d(self.state, ConwayBoard._kernel, boundary='fill', fillvalue=0)
        temp = np.where(conv_result == 3, 1, 0)
        temp[np.where(self.state == 0 & conv_result == 2)]
        self.state = temp 

    def next(self, iterations = 1):
        for _ in range(iterations):
            self.__next()
