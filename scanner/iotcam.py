from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sys
import cv2
import zbar
from PIL import Image
import sonosclient

# Debug mode
DEBUG = False
if len(sys.argv) > 1:
	DEBUG = sys.argv[-1] == 'DEBUG'

# Configuration options
if DEBUG:
    RESOLUTION = (640, 480)
else:
	RESOLUTION = (1024, 768)

# Initialise Raspberry Pi camera
camera = PiCamera()
camera.resolution = RESOLUTION

# set up stream buffer
rawCapture = PiRGBArray(camera, size=RESOLUTION)
# allow camera to warm up
time.sleep(0.1)
print("PiCamera ready")

# Initialise OpenCV window
# cv2.namedWindow("#iothack15")

print("OpenCV version: %s" % (cv2.__version__))
print("Press q to exit ...")

scanner = zbar.Scanner()

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # as raw NumPy array
    output = frame.array.copy()

    # raw detection code
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY, dstCn=0)

    # create a reader
    image = scanner.scan(gray)

    if len(image) > 0:
        symbol = image[0]
        print('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)
        sonosclient.parse(symbol.data.decode('utf-8'))

    # show the frame
    # cv2.imshow("#iothack15", output)

    # clear stream for next frame
    rawCapture.truncate(0)

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
        break

# When everything is done, release the capture
camera.close()
cv2.destroyAllWindows()
