import streamlit as st
from PIL import Image, ImageFilter

def apply_horizontal_gradient(original_image, opacity=0.5):
    # Copy of original image
    modified_image = original_image.copy()

    # size of image
    width, height = modified_image.size
    pixels = modified_image.load()

    # Apply horizontal gradient
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            alpha = int(opacity * 255 * (x / width))
            pixels[x, y] = (r, g, b, alpha)

    return modified_image

def apply_painting_effect(original_image, intensity=1.0):
    # Apply a painting effect with adjustable intensity
    painted_image = original_image.filter(ImageFilter.EDGE_ENHANCE)
    return painted_image

def main():
    st.title("Image Processing Application")
    uploaded_file = st.file_uploader("Select an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:

        original_image = Image.open(uploaded_file).convert("RGBA")
        opacity = st.slider("Select Opacity", 0.0, 1.0, 0.5, 0.1)

        # display image w/ gradient (changeable)
        modified_image = apply_horizontal_gradient(original_image, opacity)
        st.image(modified_image, caption="Gradient Image", use_column_width=True)

        # paint effect slider
        painting_intensity = st.slider("Painting Effect Intensity", 0.0, 1.0, 1.0, 0.1)

        # display image w/ paint filter (changeable)
        painted_image = apply_painting_effect(original_image)
        st.image(painted_image, caption="Painting Effect", use_column_width=True)

        # original image
        st.image(original_image, caption="Original Image", use_column_width=True)

        st.download_button("Download Modified Image", modified_image.save, args=("output_image.png",))

if __name__ == "__main__":
    main()

