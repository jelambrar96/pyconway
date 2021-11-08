from ast import copy_location
import numpy as np
from numpy.testing._private.utils import assert_

# from .board import ConwayBoard

class ConwayCanvan:

    def __init__(self, size, scale=1):
        self._bgd_color = None
        self._fgd_color = None
        self._scale = scale
        self._size = size[:2]

    def getBackground(self):
        return self._bgd_color
    
    def getForeground(self):
        return self._fgd_color

    def getScale(self):
        return self._scale


    def setBackgroud(self, color):
        # check if value is int
        temp_mat = self.__getMatrixFromColor(color)
        self._bgd_color = temp_mat


    def setForeground(self, color):
        temp_mat = self.__getMatrixFromColor(color)
        self._fgd_color = temp_mat


    def apply(self, conway_state):

        if not self._size == conway_state.shape[:2]:
            raise ValueError("ERROR: dimentions must be match!!!!!")

        temp_state = conway_state.repeat(self._scale, axis=0).repeat(self._scale, axis=1)
        # dimentions must be match!!!!!
        temp_mat = None
        if len(conway_state.shape) == 3:
            if not 3 == conway_state.shape[2]:
                raise ValueError("ERROR: inavild number of cannels!!!!!")
            temp_mat =  np.where(temp_state, self._fgd_color, self._bgd_color)
        elif len(conway_state.shape) == 2:
            temp_mat = np.empty(self._fgd_color.shape, dtype=np.uint8) 
            temp_mat[:,:,0] = np.where(temp_state, self._fgd_color[:,:,0], self._bgd_color[:,:,0])
            temp_mat[:,:,1] = np.where(temp_state, self._fgd_color[:,:,1], self._bgd_color[:,:,1])
            temp_mat[:,:,2] = np.where(temp_state, self._fgd_color[:,:,2], self._bgd_color[:,:,2])
        return temp_mat


    def __getMatrixFromColor(self, color):

        temp_mat = None

        if type(color) is int:
            if color > 255 or color < 0:
                raise ValueError("ERROR: color must be between 0 and 255" )
            temp_mat = np.full((self._size[0] * self._scale, self._size[0] * self._scale, 3), color, dtype=np.uint8)
        
        # tuple color input
        if type(color) is tuple or type(color) is list:
            if not len(color) == 3:
                raise ValueError("ERROR: only iterable of tree elements are allowed." )
            temp_mat = np.empty((self._size[0] * self._scale, self._size[0] * self._scale, 3), dtype=np.uint8)
            for i, item in enumerate(color):
                if item > 255 or item < 0:
                    raise ValueError("ERROR: color must be between 0 and 255" )
                temp_mat[:,:,i] = item

        # check if value is numpy
        if type(color) is np.ndarray:
            # assert(color.dtype == np.uint8, "ERROR: matrix must be a 8uint mat")
            color_shape = color.shape
            if not (self._size[0] * self._scale, self._size[0] * self._scale,) == color_shape[:2]:
                raise ValueError("ERROR: dimentions must be match!!!!!")
            if len(color_shape) == 2:
                temp_mat = np.empty(color_shape, dtype=np.uint8)
                temp_mat[:,:,0] = color
                temp_mat[:,:,1] = color
                temp_mat[:,:,2] = color
            if len(color_shape) == 3:
                if not color_shape[2] == 3:
                    raise ValueError( "ERROR: only three channel mat is allowed" )
                temp_mat = color
        
        return temp_mat
