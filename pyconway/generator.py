
from abc import ABC, abstractmethod
import subprocess as sp

from PIL import Image
import cv2
import numpy as np



class BasicGenerator(ABC):

    def addFrame(self, frame: np.ndarray):
        self._frame = frame

    @abstractmethod    
    def start(self):
        pass

    @abstractmethod
    def release(self):
        pass



class GifGenerator(BasicGenerator):

    def __init__(self, filename, size, fps=10):
        self._buffer = []
        self._fps = fps # default
        self._size = size
        self._filename = filename

    def addFrame(self, frame: np.ndarray):
        self._buffer.append(frame)

    def release(self):
        frames = [ Image.fromarray(item) for item in self._buffer]
        frame_one = frames[0]
        ms_by_frame = 1000 // self._fps 
        frame_one.save(self._filename, format="GIF", append_images=frames,
               save_all=True, duration=ms_by_frame, loop=0)

    def start(self):
        self._buffer = []



class VideoGenerator(BasicGenerator):

    def __init__(self):
        pass

    def start(self):
        pass

    def release(self):
        pass


class MP4VideoGenerator(BasicGenerator):

    def __init__(self, filename, size, fps):
        self._size = size
        self._fps = fps
        self._writer = None
        self._filename = filename

    def addFrame(self, frame: np.ndarray):
        if frame.shape[:2] != self._size:
            raise ValueError("ERROR: dimentions must match!!!!")
        self._frame = frame
        self._writer.write(frame)

    def start(self):
        h, w = self._size[:2]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self._writer = cv2.VideoWriter(self._filename, fourcc, self._fps, (w, h))

    def release(self):
        self._writer.release()
        pass


class PipeVideoGenerator(BasicGenerator):
    
    def __init__(self, filename, size, fps):
        self._size = size
        self._fps = fps
        self._filename = filename
        self._proc = None

    def addFrame(self, frame: np.ndarray):
        if frame.shape[:2] != self._size:
            raise ValueError("ERROR: dimentions must match!!!!")
        self._proc.stdin.write(frame.tostring())


    def start(self):
        h, w = self._size[:2]
        ffmpeg = 'ffmpeg'
        dimension = '{}x{}'.format(w, h)
        fps = str(self._fps)
        output_file = self._filename
        command = [ffmpeg,
                '-y',
                '-f', 'rawvideo',
                '-vcodec','rawvideo',
                '-s', dimension,
                '-pix_fmt', 'bgr24',
                '-r', fps,
                '-i', '-',
                '-c:a', 'acc',
                '-c:v', 'libx264',
                # '-profile:v', 'high',
                '-level:v', '4.0',
                '-x264-params', 'scenecut=0:open_gop=0:min-keyint=72:keyint=72',
                '-b:v', '3500k',
                '-maxrate', '3500k',
                '-bufsize', '3500k',
                '-preset', 'slow',
                '-crf', '23',
                '-ar',  '44100',
                '-b:a', '256k ',
                '-sn',
                '-f', 'mp4',                           
                output_file ]
        print(" ".join(command))
        self._proc = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

    def release(self):
        # self._writer.release()
        self._proc.stdin.close()
        self._proc.stderr.close()
        self._proc.wait()
        pass
"""
ffmpeg -i INPUT.MOV -vf scale=-2:720 -c:v libx264 -profile:v main -level:v 3.0 -x264-params scenecut=0:open_gop=0:min-keyint=72:keyint=72:ref=4 -c:a aac -b:v 3500k -maxrate 3500k -bufsize 3500k -r 30 -ar 44100 -b:a 256k -pass 1 -sn -f mp4 NUL && \ 
 ffmpeg -i INPUT.MOV -vf scale=-2:720 -c:v libx264 -profile:v main -level:v 3.0 -x264-params scenecut=0:open_gop=0:min-keyint=72:keyint=72:ref=4 -c:a aac -b:v 3500k -maxrate 3500k -bufsize 3500k -r 30 -ar 44100 -b:a 256k -pass 2 OUTPUT.mp4
"""

"""
ffmpeg -i INPUT.MOV -vf scale=-2:720 -c:v libx264 -profile:v main -level:v 3.0 -x264-params scenecut=0:open_gop=0:min-keyint=72:keyint=72:ref=4 -c:a aac -crf 23 -maxrate 3500k -bufsize 3500k -r 30 -ar 44100 -b:a 256k -sn -f mp4 OUTPUT.mp4
"""
"""
        command = [ffmpeg,
                '-y',
                '-f', 'rawvideo',
                '-vcodec','rawvideo',
                '-s', dimension,
                '-pix_fmt', 'bgr24',
                '-r', fps,
                '-i', '-',
                '-c:a', 'acc',
                '-vcodec', 'libx264',
                '-b:v', '3500k',
                output_file ]



                        command = [ffmpeg,
                '-y',
                '-f', 'rawvideo',
                '-s', dimension,
                '-pix_fmt', 'bgr24',
                '-r', fps,
                '-c:a', 'acc',
                '-c:v', 'libx264',
                '-profile:v', 'main',
                '-level:v', '3.0',
                '-x264-params', 'scenecut=0:open_gop=0:min-keyint=72:keyint=72',
                '-b:v', '3500k',
                '-maxrate', '3500k',
                '-bufsize', '3500k',
                '-preset', 'slow',
                '-crf', '23',
                '-sn',
                '-f', 'mp4',
                output_file
"""