
# python libraries
from typing import Tuple


# dependences
from scipy.signal import convolve2d
import numpy as np


class ConwayBoard:

    _kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)

    def __init__(self, board):
        if not np.ndim(board) == 2:
            raise ValueError('Input must both be 2-D arrays')
        self.state = board 
        # self.state = board.astype(np.uint8)
        # set default rules
        self._s_rule = [3]
        self._b_rule = [2,3]

    def getState(self):
        return self.state

    def getRules(self):
        return self._s_rule, self._b_rule

    def __next(self):
        # conv_result = convolve2d(self.state, ConwayBoard._kernel, boundary='fill', fillvalue=0)
        conv_result = convolve2d(self.state, ConwayBoard._kernel, mode="same", boundary="wrap")
        temp = np.where(self.state == 1 & conv_result in self._s_rule, 1, 0)
        temp[np.where(self.state == 0 & conv_result in self._b_rule)] = 1
        self.state = temp 

    def next(self, iterations = 1):
        for _ in range(iterations):
            self.__next()

    def setRules(self, s_rule, b_rule):
        self._s_rule = s_rule
        self._b_rule = b_rule


class ConwayBoard3C(ConwayBoard):

    def __init__(self, board):
        if not np.ndim(board) == 3:
            raise ValueError('Input must both be 3-D arrays')
        self.state = board

    def __next(self):
        pass
