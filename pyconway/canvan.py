import numpy as np

# from .board import ConwayBoard

class ConwayCanvan:

    def __init__(self, scale=1):
        self._bgd_color
        self._fgd_color
        self._scale = scale

    def getBackground(self):
        return self._bgd_color
    
    def getForeground(self):
        return self._fgd_color

    def getScale(self):
        return self._scale

    def setBackgroud(self, color):
        self._bgd_color = color

    def setForeground(self, color):
        self._fgd_color = color

    def apply(self, conway_state):
        temp_state = conway_state.repeat(self._scale, axis=0).repeat(self._scale, axis=1)
        # dimentions must be match!!!!!
        # use a broadcast if any color is a number
        return np.where(temp_state, self._fgd_color, self._bgd_color)
