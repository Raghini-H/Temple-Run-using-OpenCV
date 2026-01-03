🎮 Temple Run – Hand Gesture Control using OpenCV

Play Temple Run using hand movements captured through your webcam.
This project uses Computer Vision and Hand Gesture Recognition to control the game without a keyboard or mouse.

📌 Project Overview
This system tracks your index finger movement in real time and converts hand gestures into keyboard actions required to play Temple Run.
The project is built using:
OpenCV – video capture & image processing
MediaPipe – hand landmark detection
PyAutoGUI – keyboard control automation

✋ Gesture Controls Mapping
Hand Gesture        Game Action    Keyboard Key
LEFT palm open	     Turn Left	        ←
RIGHT palm open	     Turn Right	        →
BOTH hands open        Jump	            ↑
ONE hand fist	         Slide	          ↓
BOTH hand fist        Neutral           -

🛠 Technologies Used
Python 3.x
OpenCV
MediaPipe
PyAutoGUI
NumPy

📦 Installation
Install all required libraries using pip:
pip install opencv-python mediapipe pyautogui numpy         

▶ How to Run the Project
Open Temple Run on your PC or emulator
Make sure the game window is active
Run the Python script:
python templerun.py
Control the game using hand movements in front of your webcam
Press ESC to exit the program

⚙ How It Works
Webcam captures live video
MediaPipe detects hand landmarks
Index finger tip position is tracked
Directional movement is calculated relative to a reference point
Corresponding keyboard key is triggered using PyAutoGUI

🎯 Performance Tips
Use good lighting for accurate detection
Keep your hand clearly visible inside the camera frame
Maintain a steady reference position before moving
Adjust dead_zone and cooldown values in code if needed

📚 Learning Outcomes
Computer Vision fundamentals
Real-time hand tracking
Human–Computer Interaction (HCI)
Game automation using Python
Practical use of OpenCV and MediaPipe

🧑‍💻 Author
Raghini H
Computer Vision | Game Automation | Python
