🚗💥 Real-Time Accident Detection with YOLOv5 & Streamlit
A real-time accident detection system using YOLOv5, OpenCV, and Streamlit, enhanced with sound alerts, logging, and live dashboard updates. Designed to detect collisions between vehicles in a video stream and log incidents with frame evidence and timestamps.

🌟 Features
🔍 YOLOv5 Object Detection
Detects vehicles (cars, trucks, buses, bikes) in real-time using YOLOv5s.

🖼️ Live Video Feed with Streamlit
Displays a real-time webcam stream with frame counter and collision alerts.

💥 Collision Detection Logic
Uses bounding box overlap (IoU) to detect accidents based on object proximity.

📁 Frame Capture & Evidence Logging
Saves frames of detected accidents in an evidence/ folder with a CSV log.

🔊 Real-Time Sound Alerts
Plays an alert sound (via pygame) when a crash is detected.

🧠 Tech Stack
Tool	Purpose
YOLOv5	Real-time vehicle detection
OpenCV	Video stream handling
Streamlit	Live UI dashboard
Pandas	Logging accident data to CSV
Pygame	Playing alert sounds
Python	Overall integration and logic
📦 Installation
# Clone the repository
git clone https://github.com/your-username/accident-detection-yolov5
cd accident-detection-yolov5

# Install dependencies
pip install -r requirements.txt

# Or install manually:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install opencv-python streamlit pandas pygame
Make sure you have a working webcam and Python 3.8+.

▶️ Run the App
streamlit run app.py
Once launched:

A live camera feed will start.

When an accident is detected, you'll:

Hear a sound

See an alert in the UI

Get a frame saved in /evidence

See logs in logs.csv

📁 Project Structure
├── app.py              # Main Streamlit App
├── alert.mp3           # Sound file for alert
├── logs.csv            # Logged accident info
├── evidence/           # Captured frames
└── requirements.txt    # Dependencies
🔮 Future Improvements
🚦 Accident type classification (rear-end, side collision, etc.)

🧠 Integrate with vehicle tracking and motion estimation

🌐 Dashboard with map integration or multiple cameras

🧩 Deployable version for Raspberry Pi or Jetson Nano

📸 Preview

A live dashboard view with real-time accident detection and alerting.

📜 License
This project is licensed under the MIT License.

🤝 Contributing
Got ideas or want to improve the logic/model?
Pull requests and suggestions are always welcome!
