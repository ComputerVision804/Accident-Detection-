# app.py
import streamlit as st
import pandas as pd
from PIL import Image
import os
from detector import detect_accidents_from_camera

st.set_page_config(page_title="Accident Detection Dashboard", layout="wide")
st.title("🚗 Real-Time Accident Detection Dashboard")

st.sidebar.header("Instructions:")
st.sidebar.text("Click the button below to start accident detection on your webcam feed.")

if st.button("▶️ Run Detection on Video"):
    ("video_feed1.mp4")
    st.success("Detection Completed!")

if st.button("▶️ Start Detection"):
    st.text("Starting real-time camera feed...")
    detect_accidents_from_camera()  # Call the accident detection function for webcam feed
    st.success("Detection Completed!")

# Show accident logs and saved frames
if os.path.exists("logs.csv"):
    st.subheader("📁 Accident Evidence Log")
    df = pd.read_csv("logs.csv")
    st.dataframe(df)

    for i, row in df.iterrows():
        st.markdown(f"### 🕒 {row['timestamp']}")
        img_path = row['frame_path']
        st.image(img_path, width=600)
else:
    st.info("No accidents detected yet. Click the button above to start detection.")




