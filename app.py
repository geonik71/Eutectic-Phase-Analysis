import streamlit as st
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

# Function to remove small objects
def remove_small_objects(binary_image, min_size):
    nb_components, output, stats, _ = cv2.connectedComponentsWithStats(binary_image, connectivity=8)
    sizes = stats[1:, -1]  # Extract sizes, ignoring the background
    nb_components -= 1

    cleaned_binary = np.zeros_like(binary_image)
    for i in range(nb_components):
        if sizes[i] >= min_size:
            cleaned_binary[output == i + 1] = 255

    return cleaned_binary

# Function to convert images to a downloadable format
def convert_to_downloadable(image_array, format="PNG"):
    pil_image = Image.fromarray(image_array)
    buffered = BytesIO()
    pil_image.save(buffered, format=format)
    return buffered.getvalue()

# Streamlit app
st.markdown("<h1 style='text-align: center; font-size: 36px;'>Eutectic Phase Fraction Area Analysis</h1>", unsafe_allow_html=True)

# ⭐ GitHub Star Section
st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <h2>⭐ Enjoyed this App? Support by Starring on GitHub! ⭐</h2>
        <p style='font-size: 18px;'>If you found this tool helpful, give it a ⭐ on GitHub! Your support helps academic research! 📚</p>
        <a href='https://github.com/your-github-repo' target='_blank'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1024px-Octicons-mark-github.svg.png' width='120'>
        </a>
        <p style='font-size: 18px;'><a href='https://github.com/your-github-repo' target='_blank' style='text-decoration: none; font-weight: bold; color: #0366d6;'>Click here to star!</a> ⭐</p>
    </div>
""", unsafe_allow_html=True)

# Step 1: Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "tiff", "tif"])

if uploaded_file is not None:
    # Load the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image using Otsu's method
    _, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Remove small dots (size threshold = 300 pixels)
    min_dot_size = 300
    cleaned_binary = remove_small_objects(otsu_thresh, min_dot_size)

    # Calculate eutectic phase fractions
    eutectic_pixels_before = np.sum(otsu_thresh == 255)
    eutectic_fraction_before = eutectic_pixels_before / otsu_thresh.size

    eutectic_pixels_after = np.sum(cleaned_binary == 255)
    eutectic_fraction_after = eutectic_pixels_after / cleaned_binary.size

    # Step 2: Display result images in one row and 3 columns
    col1, col2, col3 = st.columns(3)

    # Format selection dropdown
    image_format = st.selectbox("Select download format:", ["PNG", "JPG", "JPEG", "TIFF", "TIF"])

    with col1:
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_container_width=True)
        original_image_download = convert_to_downloadable(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), image_format)
        st.download_button(
            label=f"Download Original Image ({image_format})",
            data=original_image_download,
            file_name=f"original_image.{image_format.lower()}",
            mime=f"image/{image_format.lower()}"
        )

    with col2:
        st.image(otsu_thresh, caption="Thresholded Image (Otsu)", use_container_width=True, channels="GRAY")
        otsu_thresh_download = convert_to_downloadable(otsu_thresh, image_format)
        st.download_button(
            label=f"Download Thresholded Image ({image_format})",
            data=otsu_thresh_download,
            file_name=f"otsu_thresh.{image_format.lower()}",
            mime=f"image/{image_format.lower()}"
        )

    with col3:
        st.image(cleaned_binary, caption="Cleaned Image (Dots Removed)", use_container_width=True, channels="GRAY")
        cleaned_binary_download = convert_to_downloadable(cleaned_binary, image_format)
        st.download_button(
            label=f"Download Cleaned Image ({image_format})",
            data=cleaned_binary_download,
            file_name=f"cleaned_binary.{image_format.lower()}",
            mime=f"image/{image_format.lower()}"
        )

    # Step 3: Display the eutectic phase fractions with custom styling
    st.markdown(f"<div style='font-size: 24px; font-weight: bold; color: #ff6347; text-align: center; padding: 10px; background-color: #f0f8ff; border-radius: 10px;'>Eutectic Phase Fraction (Before Cleaning): {eutectic_fraction_before:.4%}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 24px; font-weight: bold; color: #ff6347; text-align: center; padding: 10px; background-color: #f0f8ff; border-radius: 10px;'>Eutectic Phase Fraction (After Cleaning): {eutectic_fraction_after:.4%}</div>", unsafe_allow_html=True)

# Explanation Section
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2 style='font-size: 24px;'>How the Code Works</h2>", unsafe_allow_html=True)
    st.markdown("""
        <ul style='font-size: 18px;'>
            <li><strong>Step 1:</strong> Upload an image that contains the eutectic phase.</li>
            <li><strong>Step 2:</strong> The image is converted to grayscale to simplify processing.</li>
            <li><strong>Step 3:</strong> Otsu's thresholding method is applied to separate the eutectic phase from the background.</li>
            <li><strong>Step 4:</strong> Small objects are removed from the thresholded image to clean it up.</li>
            <li><strong>Step 5:</strong> The eutectic phase fraction is calculated based on the proportion of pixels in the eutectic phase.</li>
        </ul>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<h2 style='font-size: 24px;'>Description of Eutectic Phase</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p style='font-size: 18px;'>The eutectic phase refers to a specific mixture of two materials that, when solidified, form a unique microstructure. The eutectic phase often plays an important role in determining the physical properties of alloys. This analysis helps in identifying and quantifying the eutectic phase in materials like metals, where the distribution and volume fraction of this phase can influence the mechanical properties of the final product.</p>
    """, unsafe_allow_html=True)
