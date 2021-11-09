
from abc import ABC, abstractmethod


from PIL import Image
import numpy as np



class BasicGenerator(ABC):

    def setFPS(self, fps: int):
        self._fps = fps
    
    def setFrame(self, frame: np.ndarray):
        self._frame = frame

    @abstractmethod    
    def save(self, filename):
        pass

    @abstractmethod    
    def start(self):
        pass

    @abstractmethod
    def release(self):
        pass



class GifGenerator(BasicGenerator):

    def __init__(self):
        self._buffer = []
        self._fps = 10 # default

    def release(self):
        self._buffer = []
        
    def save(self, filename):
        frames = [ Image.fromarray(item) for item in self._buffer]
        frame_one = frames[0]
        ms_by_frame = 1000 // self._fps 
        frame_one.save(filename, format="GIF", append_images=frames,
               save_all=True, duration=ms_by_frame, loop=0)

    def start(self):
        self._buffer = []



class VideoGenerator(BasicGenerator):

    def __init__(self):
        pass

    def save(self, filename):
        pass

    def start(self):
        pass

    def release(self):
        pass
