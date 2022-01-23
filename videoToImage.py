# Importing all necessary libraries
import cv2
import os
import os.path
from PIL import Image
import sys

# Read the videos from specified path
if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Error specifing parameters ")
  else:
    videoPath = sys.argv[1]
    outputDir = sys.argv[2]

    currentFrame = 0
    cam = cv2.VideoCapture(videoPath)
    if not os.path.exists(outputDir):
      os.makedirs(outputDir)

    while(True):
      cam.set(cv2.CAP_PROP_POS_MSEC, (currentFrame*5000))
      # reading from frame
      ret, frame = cam.read()

      if ret:
          # if video is still left continue creating images
          name = outputDir +'/' +str(currentFrame) + '.jpg'
          print('Creating...' + name)

          # writing the extracted images
          cv2.imwrite(name, frame)

          # increasing counter so that it will
          # show how many frames are created
          currentFrame += 1
      else:
          break

    cam.release()

    cv2.destroyAllWindows()
