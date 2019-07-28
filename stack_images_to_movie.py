import cv2
import os
import string
from natsort import natsorted
# Arguments
dir_path = 'D:\Documents\OneDrive - UGent\VIB-UGent PhD\__Experiments\E007\E007.2\Analysis\Prova'
ext = ".jpeg"
output = "D:\\Documents\\OneDrive - UGent\\VIB-UGent PhD\\__Experiments\\E007\\E007.2\\Analysis\\Prova\\video.avi"
fps = 10.0

images = os.listdir(path)

###
images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)
images = natsorted(images)

# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, fps, (width, height))

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)

    out.write(frame) # Write out frame to video

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))
