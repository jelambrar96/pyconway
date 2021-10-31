
# python libraries
from typing import Tuple


# dependences
from scipy.signal import convolve2d
import numpy as np


class ConwayBoard:

    _kernel = np.array([1, 1, 1], [1, 0, 1], [1, 1, 1])

    def __init__(self, board):
        if not np.ndim(board) == 2:
            raise ValueError('Input must both be 2-D arrays')
        self.state = board 

    def getState(self):
        return self.state

    def __next(self):
        conv_result = convolve2d(self.state, ConwayBoard._kernel, boundary='fill', fillvalue=0)
        temp = np.where(conv_result == 3, 1, 0)
        temp[np.where(self.state == 0 & conv_result == 2)] = 1
        self.state = temp 

    def next(self, iterations = 1):
        for _ in range(iterations):
            self.__next()
