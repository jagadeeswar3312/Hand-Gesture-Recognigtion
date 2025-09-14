🤚 Hand Gesture Recognition Using Python, OpenCV, and MediaPipe

A real-time hand gesture recognition system that captures video from a webcam, detects hand landmarks using MediaPipe, and classifies gestures such as Fist, Open Palm, Thumbs Up, OK Sign, and Love Sign.

This project demonstrates the integration of Computer Vision and Rule-based ML for building gesture-controlled applications.

✨ Features

📸 Real-time hand detection & tracking using MediaPipe’s pretrained model

🎥 Webcam video capture & display with OpenCV

🖐️ Gesture classification with custom landmark analysis

✅ Recognized gestures:

Fist (all fingers folded)

Open Palm (all fingers extended)

Thumbs Up (only thumb extended)

OK Sign (thumb & index fingertips touching)

Love Sign (index & pinky extended)

📝 Gesture name displayed live on the video feed

⚙️ How It Works

Video Capture – OpenCV continuously reads frames from the webcam

Hand Landmark Detection – MediaPipe detects 21 key landmarks of the hand

Gesture Analysis – Rules check which fingers are open/closed and distances between landmarks

Gesture Classification – Maps landmark patterns to predefined gestures

Visualization – OpenCV overlays landmarks & recognized gesture name on the video

🛠️ Requirements

Python 3.x

OpenCV
 (opencv-python)

MediaPipe
 (mediapipe)

🚀 Installation
# Clone this repository
git clone https://github.com/your-username/hand-gesture-recognition.git
cd hand-gesture-recognition

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install opencv-python mediapipe

▶️ Usage
python hand_gesture.py


A window opens with live webcam feed

Show different gestures to test detection

Press ESC to exit

🎯 Learning Outcomes

Work with live video capture using OpenCV

Use MediaPipe for real-time hand tracking

Process hand landmarks for gesture recognition

Build rule-based classification logic

Apply Python for computer vision & HCI projects

💡 Applications

Gesture-based user interfaces

Sign language recognition assistive tools

Touchless device/software control

Interactive education & entertainment apps

📜 License

This project is open-source and available for educational & personal use.
