from chatgpt_generated import cartoonize
import cv2 as cv

# Load the image
img = cv.imread("./data/baboon.tiff")

# Display the resulting image
cv.imshow("Photo Cartoonize", cartoonize(img))
cv.waitKey(0)
cv.destroyAllWindows()