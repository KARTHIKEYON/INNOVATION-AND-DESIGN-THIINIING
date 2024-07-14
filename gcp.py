import streamlit as st
import requests

# Streamlit app
st.title("Deep Fake Detection")

# File upload widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Deep fake detection button
if st.button("Detect Deep Fake"):
    if uploaded_file is not None:
        st.write("Detecting...")
        # Define the endpoint URL
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        # Define the API key
        API_KEY = "AIzaSyB97RBGR0Clr1NUUzH8jkIjrdAWuZTHZp0"
        # Prepare the payload
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"image": uploaded_file.read()}
                    ]
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        # Send the POST request
        response = requests.post(f"{url}?key={API_KEY}", json=payload, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            # Display the detection result
            st.write("Detection Result:")
            st.write(result)
        else:
            st.error(f"Error: {response.status_code}. Unable to perform deep fake detection.")
    else:
        st.warning("Please upload an image.")
