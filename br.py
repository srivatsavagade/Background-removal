import streamlit as st
from rembg import remove
from PIL import Image

def main():
    st.title("Background Removal App")

    image_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Original Image', use_column_width=True)

        if st.button("Remove Background"):
            with st.spinner("Removing background..."):
                result_image = remove(image)
                st.image(result_image, caption='Background Removed', use_column_width=True)

if __name__ == "__main__":
    main()
