# Eutectic Phase Analysis Streamlit App

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
