import cv2
import pytesseract # or import easyocr

# Load the image
image = cv2.imread('test_image4.png')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = (0, 100, 100)
upper = (360, 256, 256)
mask = cv2.inRange(hsv_image, lower, upper)

colored_text_only = cv2.bitwise_and(image, image, mask=mask)

gray_colored_text = cv2.cvtColor(colored_text_only, cv2.COLOR_BGR2GRAY)

_, binary_colored_text = cv2.threshold(gray_colored_text, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

gray_colored_text = cv2.cvtColor(colored_text_only, cv2.COLOR_BGR2GRAY)

# Using pytesseract
text = pytesseract.image_to_string(binary_colored_text)
print(text)

# Using easyocr (if installed)
# reader = easyocr.Reader(['en']) # Specify language(s)
# results = reader.readtext(binary_colored_text)
# for (bbox, text, prob) in results:
#     print(text)

# Define range for white color in HSV
# These values might need adjustment based on your image's specific "white"
lower_white = (0, 0, 150)  # Adjust V (Value) for brightness
upper_white = (255, 50, 255) # Adjust S (Saturation) to exclude grayish areas

# Create a mask to isolate white regions
mask = cv2.inRange(hsv_image, lower_white, upper_white)

# Apply the mask to the original image
white_text_only = cv2.bitwise_and(image, image, mask=mask)

# Convert the masked image to grayscale (Tesseract often performs better on grayscale)
gray_white_text = cv2.cvtColor(white_text_only, cv2.COLOR_BGR2GRAY)

# Apply a threshold to make the white text stand out even more
_, thresh = cv2.threshold(gray_white_text, 200, 255, cv2.THRESH_BINARY)

# Use Tesseract to extract text from the thresholded image
extracted_text = pytesseract.image_to_string(thresh)
extracted_list = extracted_text.split('\n')
substring_to_keep = "Dist"
filtered_list = [s for s in extracted_list if substring_to_keep in s]
print(filtered_list)