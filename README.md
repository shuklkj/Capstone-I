# Facial-Recognition-Enabled-Drones-Enhancing-Autonomous-Identification-and-Security


The Facial Recognition Drone is a cutting-edge technological solution that combines the advancements in robotics, artificial intelligence, and computer vision to enable autonomous and intelligent aerial surveillance. This drone is equipped with a sophisticated facial recognition system that can identify and match individuals' faces with a pre-existing database. By leveraging object detection, facial analysis, and identification algorithms, the drone can perform tasks such as identifying known or wanted criminals in a crowd, conducting surveillance in secured areas, and locating missing persons in various scenarios.


Tello Drone Face Tracking
This repository contains code for real-time face tracking using a DJI Tello drone. The drone captures video frames, detects a face, and then uses a PID controller to move itself and keep the face in the center of the frame.

Features:
Real-time face tracking using Haar cascades.
Use of PID controllers for smooth and accurate drone movement.
Option to save the video feed to an MP4 file.
Separate processes for face tracking, video display, and video recording for efficient multitasking.
Graceful shutdown on keyboard interrupts.
Dependencies:
cv2: OpenCV library for computer vision tasks.
djitellopy: Python interface for DJI Tello drone.
imutils: Image processing utility functions.
multiprocessing: Standard library for parallel execution of tasks.
How to Run:
Ensure you have all dependencies installed.
Clone this repository:
bash
Copy code
git clone <repository_link>
Navigate to the repository's directory and run the main script:
php
Copy code
cd <repository_directory>
python <script_name>.py
Code Overview:
signal_handler: Handles keyboard interrupts to ensure the Tello drone lands safely and any video writers release their resources.
track_face_in_video_feed: The main function responsible for controlling the drone, detecting faces, and using PID controllers to move the drone.
show_video: Displays the video feed in a window using OpenCV.
video_recorder: Saves the video frames to an MP4 file.
The main portion of the code sets up multiprocessing, creating separate processes for the three main tasks and ensuring their coordinated execution.

Configuration:
There are several parameters you can adjust:

TARGET_FACE_SIZE: Target size for the detected face in the video frame.
max_speed_limit: Maximum speed that the drone will send as a command.
Various PID controller parameters for pan, tilt, and distance.