import picamera
import picamera.array
import numpy as np
import time

class MyMotionDetector(picamera.array.PiMotionAnalysis):
    def analyse(self, a):
        a = np.sqrt(
            np.square(a['x'].astype(np.float)) +
            np.square(a['y'].astype(np.float))
            ).clip(0, 255).astype(np.uint8)
        # If there're more than 10 vectors with a magnitude greater
        # than 60, then say we've detected motion
        if (a > 60).sum() > 10:
            for filename in camera.capture_continuous('Spy{counter:03d}.jpg', use_video_port=True):
                print('Motion detected!')
                print('Captured %s' % filename)
                # time.sleep(2)
                # wait 5 minutes


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    camera.start_recording(
        '/dev/null', format='h264',
        motion_output=MyMotionDetector(camera)
        )
    camera.wait_recording(300)
    camera.stop_recording()