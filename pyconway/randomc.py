import numpy as np

def createRandomState(size, threshold=0.5):
    board = np.random.random(size)
    return np.where(board >= threshold, 0, 1).astype(np.uint8)
