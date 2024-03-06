import numpy as np
import cv2

def calculate_NDVI(image):
    # Convert image to float32
    image = image.astype(np.float32)
    
    # Extract bands
    red, nir = image[:,:,1], image[:,:,2]
    
    # Calculate NDVI
    NDVI = (nir - red) / (nir + red)
    
    return NDVI

# Read an RGB image (make sure it has NIR and red bands)
image_path = "testImage.jpg"  # Specify your image path
image = cv2.imread(image_path)

# Calculate NDVI
NDVI_image = calculate_NDVI(image)

# Display the NDVI image
cv2.imshow('NDVI Image', NDVI_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

