import cv2
from skimage import measure, color
import numpy as np


def calculate_greenness(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper green color thresholds in HSV
    lower_green = np.array([30, 50, 50])
    upper_green = np.array([90, 255, 255])

    # Create a mask for green pixels within the specified range
    mask = cv2.inRange(hsv_img, lower_green, upper_green)

    # Calculate the percentage of green pixels in the image
    greenness = np.count_nonzero(mask) / (mask.shape[0] * mask.shape[1])

    return greenness

greenness = calculate_greenness("932.png")
print(greenness)
