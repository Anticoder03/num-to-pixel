import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import io

st.title("Number Image → Pixelated Converter")

st.write("Upload an image of a number and convert it into a 28x28 pixelated format.")

uploaded_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

if uploaded_file is not None:

    # Load image
    img = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(img, use_column_width=True)

    # Convert to RGB
    img = img.convert("RGB")

    # Convert to grayscale
    img_gray = img.convert("L")

    # Resize to MNIST size
    img_28 = img_gray.resize((28,28))

    st.subheader("28x28 Pixelated Image")
    st.image(img_28, width=200)

    # Convert to numpy array
    pixel_array = np.array(img_28)

    st.subheader("Pixel Matrix (28x28)")
    st.write(pixel_array)

    # Plot visualization
    fig, ax = plt.subplots()
    ax.imshow(pixel_array, cmap="gray")
    ax.set_title("Pixel Visualization")
    ax.axis("off")

    st.pyplot(fig)

    # Download button
    buffer = io.BytesIO()
    img_28.save(buffer, format="PNG")

    st.download_button(
        label="Download Pixelated Image",
        data=buffer.getvalue(),
        file_name="pixelated_28x28.png",
        mime="image/png"
    )