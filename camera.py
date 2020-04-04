import os
import cv2
from base_camera import BaseCamera
import time


class Camera(BaseCamera):
    video_source = 1

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            start = time.time()
            # read current frame
            _, img = camera.read()

            cv2.putText(img, str(1.0/ (time.time() - start)), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()