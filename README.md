# Eutectic Phase Area Fraction Calculator Streamlit App

This Streamlit app performs eutectic phase analysis on images to identify and calculate the eutectic phase fraction in materials, particularly in alloys. The app uses image processing techniques to clean the images and remove unwanted noise, providing a more accurate representation of the eutectic phase.

## Features

- Upload an image containing the eutectic phase.
- Convert the image to grayscale and apply Otsu's thresholding to isolate the eutectic phase.
- Remove small objects (noise) to clean the image.
- Display the original, thresholded, and cleaned images.
- Calculate and display the eutectic phase fraction before and after cleaning.
- Download the processed images in PNG format.

## Requirements

To run this app locally or on a server, ensure you have the following Python libraries installed. You can install them using the `requirements.txt` file provided.

### Required Libraries

- **streamlit**: Main framework for building the web app.
- **opencv-python-headless**: For image processing.
- **numpy**: For numerical operations.
- **pillow**: For image manipulation.

You can install all dependencies with the following command:

```bash
pip install -r requirements.txt
```
## Features Explained

### Image Upload
Upload an image that contains the eutectic phase, such as a metallurgical micrograph. The image will be processed to calculate the eutectic phase fraction.

### Image Processing
The app applies Otsu’s thresholding to separate the eutectic phase from the background.  
Small unwanted objects (like noise) are removed from the image to clean it up and provide a more accurate analysis.

### Results
Three images are displayed:
- **Original Image**: The uploaded image.
- **Thresholded Image (Otsu)**: The result of thresholding to separate the eutectic phase.
- **Cleaned Image (Dots Removed)**: The thresholded image after removing small objects/noise.  

The eutectic phase fraction before and after cleaning is displayed as percentages.

### Download Images
You can download the processed images in PNG format by clicking the download buttons below each image.
### Acknowledgments
- **This project uses OpenCV for image processing and Streamlit for creating the web interface.
- **Special thanks to the contributors and open-source community.
