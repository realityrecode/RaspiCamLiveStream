import io
import time
import picamera
from VideoStream.base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.vflip = True
            camera.framerate = 22
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
