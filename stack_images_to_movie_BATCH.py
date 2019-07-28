import cv2
import os
import string
from natsort import natsorted
# Arguments
path = 'D:\Documents\OneDrive - UGent\VIB-UGent PhD\__Experiments\E007\E007.2\Analysis\Output'
ext = ".jpeg"
output = "D:\\Documents\\OneDrive - UGent\\VIB-UGent PhD\\__Experiments\\E007\\E007.2\\Analysis\\Output\\Movies\\"
ext_video = ".avi"
fps = 10.0

## Change this number based on the file names. Put a number that will remove all the characters from the right of the name up to the sequential numbers
num_character_to_remove = 11

images = os.listdir(path)
# Determine the width and height from the first image
image_path = os.path.join(path, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case

###
images_to_parse = []
grouping_names = []
for image in images:
    if image.endswith(ext):
        images_to_parse.append(image)
        print(image[:-num_character_to_remove])
for image in images_to_parse:
	grouping_names.append(image[:-num_character_to_remove].rstrip(string.digits))

unique_groups = set(grouping_names)

grouped_images = []
for group in unique_groups:
	for image in images_to_parse:
		if group in image:
			grouped_images.append(image)

	grouped_images = natsorted(grouped_images)
	out = cv2.VideoWriter(output+group[:-2]+ext_video, fourcc, fps, (width, height))
	for image in grouped_images:
	    image_path = os.path.join(path, image)
	    frame = cv2.imread(image_path)

	    out.write(frame) # Write out frame to video

	    cv2.imshow('video',frame)
	    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
	        break

	# Release everything if job is finished
	out.release()
	cv2.destroyAllWindows()

	print("The output video is {}".format(output))
	grouped_images = []







