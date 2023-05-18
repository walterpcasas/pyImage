import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(height, width, channels) = image.shape[:3]

print("width: {} px".format(width))
print("height: {} px".format(height))
print("channels: {} px".format(channels))

## Visualize image
#cv2.imshow("Image", image)
#cv2.waitKey(0)

## Save image in JPG
#cv2.imwrite("output.jpg", image)
