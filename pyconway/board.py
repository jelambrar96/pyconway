
# python libraries
from typing import Tuple, overload


# dependences
from scipy.signal import convolve2d, convolve
import numpy as np


class ConwayBoard:

    _kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)

    def __init__(self, board):
        if not np.ndim(board) == 2:
            raise ValueError('Input must both be 2-D arrays')
        self.state = board.copy()
        # self.state = board.astype(np.uint8)
        # set default rules
        self._s_rule = np.array([2, 3])
        self._b_rule = np.array([3])

    def getState(self):
        return self.state

    def getRules(self):
        return self._s_rule, self._b_rule

    def __next(self):
        conv_result = convolve2d(self.state, ConwayBoard._kernel, mode='same', boundary='fill', fillvalue=0)
        temp0 = np.logical_and(self.state == True, np.isin(conv_result, self._s_rule))
        temp1 = np.logical_and(self.state == False, np.isin(conv_result, self._b_rule))
        self.state = np.logical_or(temp0, temp1) 

    def next(self, iterations = 1):
        for _ in range(iterations):
            self.__next()

    def setRules(self, s_rule, b_rule):
        self._s_rule = np.array(s_rule)
        self._b_rule = np.array(b_rule)


class ConwayBoard3C(ConwayBoard):

    def __init__(self, board):
        if not np.ndim(board) == 3:
            raise ValueError('Input must both be 3-D arrays')
        self.state = board.copy()
        self._s_rule = np.array([2, 3])
        self._b_rule = np.array([3])

    @overload
    def next(self, iterations = 1):
        channels = self.state.shape[2]
        for i in range(channels):
            temp_state = self.state[:,:,i]
            for j in range(iterations):
                conv_result = convolve2d(temp_state, ConwayBoard._kernel, mode='same', boundary='fill', fillvalue=0)
                temp0 = np.logical_and(temp_state == True, np.isin(conv_result, self._s_rule))
                temp1 = np.logical_and(temp_state == False, np.isin(conv_result, self._b_rule))
                temp_state = np.logical_or(temp0, temp1) 
            self.state[:,:,i] = temp_state


class ConwayBoard3D(ConwayBoard):

    _kernel_3d = np.ones((3,3,3))

    def __init__(self, board):
        if not np.ndim(board) == 3:
            raise ValueError('Input must both be 3-D arrays')
        self.state = board.copy()
        self._s_rule = np.array([2, 3])
        self._b_rule = np.array([3])

    @overload
    def __next(self):
        conv_result = convolve(self.state, ConwayBoard3D._kernel_3d, mode='same', boundary='fill', fillvalue=0) - self.state
        temp0 = np.logical_and(self.state == True, np.isin(conv_result, self._s_rule))
        temp1 = np.logical_and(self.state == False, np.isin(conv_result, self._b_rule))
        self.state = np.logical_or(temp0, temp1)
