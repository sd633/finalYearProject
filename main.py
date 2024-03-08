import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_nir_band(rgb_image_path):
    # Read the RGB image
    rgb_image = cv2.imread(rgb_image_path, cv2.IMREAD_UNCHANGED)

    # Extract the Red and Blue channels from the RGB image
    red_channel = rgb_image[:, :, 2]
    blue_channel = rgb_image[:, :, 0]

    # Compute the synthetic NIR band (Here, we are simply taking the average of Red and Blue channels)
    synthetic_nir = (red_channel.astype(np.float32) + blue_channel.astype(np.float32)) / 2

    # Convert the synthetic NIR band to uint8
    synthetic_nir = synthetic_nir.astype(np.uint8)

    # Stack the RGB channels along with the synthetic NIR band
    rgb_with_nir = cv2.merge((rgb_image[:, :, 0], rgb_image[:, :, 1], red_channel, synthetic_nir))

    return rgb_with_nir

def calculate_ndvi(rgb_with_nir):
    # Extract NIR and Red bands
    nir_band = rgb_with_nir[:, :, 3].astype(np.float32)
    red_band = rgb_with_nir[:, :, 2].astype(np.float32)

    # Replace NaN values with 0
    nir_band = np.nan_to_num(nir_band)
    red_band = np.nan_to_num(red_band)

    # Compute NDVI
    denominator = nir_band + red_band
    ndvi = np.where(
        denominator == 0.,  # Check for zero denominators
        0,                 # Assign 0 where denominator is 0 to avoid division by zero
        (nir_band - red_band) / denominator
    )

    return ndvi


# def calculate_ndvi(rgb_with_nir):
#     # Extract NIR and Red bands
#     nir_band = rgb_with_nir[:, :, 3].astype(np.float32)
#     red_band = rgb_with_nir[:, :, 2].astype(np.float32)

#     # Compute NDVI
#     denominator = nir_band + red_band
#     ndvi = np.zeros_like(nir_band)  # Initialize NDVI array

#     for i in range(ndvi.shape[0]):
#         for j in range(ndvi.shape[1]):
#             if denominator[i, j] == 0:
#                 ndvi[i, j] = 0  # Handle division by zero
#             else:
#                 ndvi[i, j] = (nir_band[i, j] - red_band[i, j]) / denominator[i, j]

#             # Print NDVI value for each pixel
#             print(f"Pixel ({i}, {j}): NDVI = {ndvi[i, j]}")

#     return ndvi



def display_ndvi(ndvi):
    plt.figure(figsize=(10, 10))
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar()
    plt.title('NDVI Image')
    plt.show()

def save_ndvi(ndvi, output_path):
    # Save NDVI image using OpenCV
    cv2.imwrite(output_path, ndvi)

if __name__ == "__main__":
    # Input RGB image path
    rgb_image_path = 'testImage.jpg'

    # Add NIR band to RGB image
    rgb_with_nir = add_nir_band(rgb_image_path)

    # Calculate NDVI
    ndvi = calculate_ndvi(rgb_with_nir)

    # Display NDVI image
    display_ndvi(ndvi)

    # Save NDVI image
    output_path = 'ndvi_output.jpg'
    save_ndvi(ndvi, output_path)

    # Print NDVI values
    print("NDVI Values:")
    print(ndvi)
