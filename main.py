import streamlit as st
import requests

# API_KEY = "YOUR_API_KEY"
API_KEY = "AIzaSyB97RBGR0Clr1NUUzH8jkIjrdAWuZTHZp0"
def is_deep_fake(image):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"
    files = {"file": image}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        result = response.json()
        # Extract and return relevant information from the response
        return result.get("contents", [{}])[0].get("parts", [{}])[0].get("text", "Unable to determine")
    else:
        return "Error: Unable to determine"


def main():
    st.title("Deep Fake Detection")

    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Checking if it's a deep fake...")

        # Check if the image is a deep fake
        result = is_deep_fake(uploaded_image)

        st.write("Result:", result)


if __name__ == "__main__":
    main()
