# import numpy as np
# import cv2

# def calculate_VARI(image):
#     # Convert image to float32
#     image = image.astype(np.float32)
    
#     # Extract bands
#     blue, green, red = image[:,:,0], image[:,:,1], image[:,:,2]
    
#     # Calculate VARI
#     VARI = (green - red) / (green + red - blue)
    
#     return VARI

# # Read an RGB image
# image_path = "testImage.jpg"  # Specify your image path
# image = cv2.imread(image_path)

# # Calculate VARI
# VARI_image = calculate_VARI(image)

# # Display the VARI image
# cv2.imshow('VARI Image', VARI_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import numpy as np
import cv2

def calculate_VARI(image):
    # Convert image to float32
    image = image.astype(np.float32)
    
    # Extract bands
    blue, green, red = image[:,:,0], image[:,:,1], image[:,:,2]
    
    # Calculate VARI
    VARI = (green - red) / (green + red - blue + 1e-8)  # Adding a small epsilon to avoid division by zero
    
    return VARI

# Read an RGB image
image_path = "testImage.jpg"  # Specify your image path
image = cv2.imread(image_path)

# Calculate VARI
VARI_image = calculate_VARI(image)

# Display the VARI image
cv2.imshow('VARI Image', VARI_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print VARI values
print("VARI values:")
print(VARI_image)