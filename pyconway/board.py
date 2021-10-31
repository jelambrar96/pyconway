
# python libraries
from typing import Tuple


# dependences
from scipy.signal import convolve2d
import numpy as np


class ConwayBoard:

    _kernel = np.array([1, 1, 1], [1, 0, 1], [1, 1, 1])

    def __init__(self, size=None, board=None):
        assert(size is not None or board is not None, 
                "Both arguments have not be None at the same time")
        if size is None and board is not None:
            self.state = board 
            self.size = board.shape
        elif size is not None and board is None:
            self.size = size
            self.state  = np.zeros(size, dtype=bool)
        elif size is not None and board is not None:
            assert(size == board.shape, "Size and board does not Match")
            self.state = board 
            self.size = board.shape

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
