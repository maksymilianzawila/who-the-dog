import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import altair as alt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.optimizers import Adam

# Load the pre-trained model with labels of breeds
model = load_model("dog_breed.h5")
model.compile(loss = 'categorical_crossentropy', optimizer = Adam(0.0001),metrics=['accuracy'])
labels_all = pd.read_csv('./labels.csv')
breeds = labels_all['breed'].unique()
formatted_breeds = [breed.replace('_', ' ').title() for breed in breeds]

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to the input size expected by the model
    image = img_to_array(image)  # Convert to array
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize to [0, 1]
    return image

# Function to predict dog breed using the loaded model
def predict_dog_breed(image):
    image = preprocess_image(image)
    predictions = model.predict(image)[0]
    confidences = [round(float(pred), 2) for pred in predictions]
    return list(zip(formatted_breeds, confidences))

st.set_page_config(
    page_title="Who The Dog? 🐾",
    page_icon="🐶",
    layout="centered"
)

st.title("🐾 Who The Dog?")
st.subheader("Upload a photo of your dog, and we'll identify its breed!")

uploaded_file = st.file_uploader("Upload a dog image (JPEG or PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    placeholder = st.empty()

    with st.spinner("Analyzing..."):
        placeholder.text("Analyzing the image...")
        predictions = predict_dog_breed(image)

    placeholder.empty()

    top_breed, top_confidence = max(predictions, key=lambda x: x[1])

    # Display the top prediction
    st.success(f"🎉 The predicted dog breed is: **{top_breed}**")
    st.metric(label="Confidence", value=f"{top_confidence * 100:.0f}%")

    # Show Top-N Predictions in a Table
    st.write("### Top Predictions")
    df = pd.DataFrame(predictions, columns=["Breed", "Confidence"])
    df["Confidence (%)"] = (df["Confidence"] * 100).round(2)
    df = df.reset_index(drop=True)
    df.index = df.index + 1
    st.dataframe(df[["Breed", "Confidence (%)"]])

    # Display Confidence Breakdown as a Chart
    st.write("### Confidence Breakdown")
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Confidence", title="Confidence"),
        y=alt.Y("Breed", sort="-x", title="Breed"),
        color=alt.Color("Confidence", scale=alt.Scale(scheme="blues"), legend=None),
        tooltip=["Breed", "Confidence (%)"],
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.info("Please upload an image to get started.")