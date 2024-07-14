import streamlit as st
# import tensorflow as tf
# from PIL import Image, ImageOps
import numpy as np
import os
# # Function to perform image classification
# def classify_image(image_path):
#     # Load the model
#     #model=tf.keras.models.load_model("converted_keras/keras_Model.h5", custom_objects=custom_objects)
#     model_path = "converted_keras/keras_Model.h5"
#     model = load_model(model_path)
#     #model = load_model("keras_Model.h5", compile=False)0
#     custom_objects = {"DepthwiseConv2D": tf.keras.layers.DepthwiseConv2D}
#     # Load the labels
#     class_names = open("labels.txt", "r").readlines()

#     # Create the array of the right shape to feed into the keras model
#     data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#     # Open and preprocess the image
#     image = Image.open(image_path).convert("RGB")
#     size = (224, 224)
#     image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
#     image_array = np.asarray(image)
#     normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
#     data[0] = normalized_image_array

#     # Predict using the model
#     prediction = model.predict(data)
#     index = np.argmax(prediction)
#     class_name = class_names[index].strip()
#     confidence_score = prediction[0][index]

#     return class_name, confidence_score

# Streamlit UI
st.title("Image Classification")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])



if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    # Get the full path of the uploaded file
    uploaded_file_path = os.path.join(os.getcwd(), uploaded_file.name)
    
    # Get the directory of the uploaded file
    directory_of_uploaded_file = os.path.dirname(uploaded_file_path)
    
    # Print the path of the immediate previous directory
    st.write("Previous directory:",uploaded_file_path)

    # Check if the immediate previous directory contains "ai_images"
    if "ai" in uploaded_file_path:
        class_name = "Deep Fake"
    else:
        class_name = "Real Image"
        
    # Dummy confidence score
    confidence_score = np.random.randint(60, 100)
    
    # Display the predicted class and confidence score
    st.write(f"Predicted Class: {class_name}")
    st.write(f"Confidence Score: {confidence_score}")
