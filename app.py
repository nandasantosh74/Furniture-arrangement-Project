import streamlit as st
import numpy as np
import tensorflow as tf
from generate_layout import generate_layout

# ✅ Load trained Keras model only once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("furniture_model.keras")

model = load_model()  # ✅ Load once for speed

st.title("🎩 AI Furniture Arrangement (ML Model)")

# ✅ User Inputs
room_width = st.slider("Room Width", 3, 10, 5)
room_height = st.slider("Room Height", 3, 10, 5)
num_furniture = st.slider("Number of Furniture Items", 1, 5, 3)

# ✅ Use Streamlit session state to store predictions
if "predictions" not in st.session_state:
    st.session_state.predictions = None

if st.button("Generate Layout"):
    # ✅ Normalize input
    input_data = np.array([[room_width, room_height, num_furniture]])
    input_data = input_data / (np.max(input_data, axis=0) + 1e-8)  # Prevent division by zero

    # ✅ Predict furniture positions
    st.session_state.predictions = model.predict(input_data)

    # ✅ Denormalize output
    st.session_state.predictions *= np.array([room_width, room_height] * (st.session_state.predictions.shape[1] // 2))

# ✅ Generate and display the layout only once
if st.session_state.predictions is not None:
    fig = generate_layout(room_width, room_height, num_furniture)  # ✅ No extra argument
    st.pyplot(fig)

# ✅ Check if GPU is being used
print(tf.config.list_physical_devices('GPU'))
