# Facial-Recognition-Enabled-Drones-Enhancing-Autonomous-Identification-and-Security


The Facial Recognition Drone is a cutting-edge technological solution that combines the advancements in robotics, artificial intelligence, and computer vision to enable autonomous and intelligent aerial surveillance. This drone is equipped with a sophisticated facial recognition system that can identify and match individuals' faces with a pre-existing database. By leveraging object detection, facial analysis, and identification algorithms, the drone can perform tasks such as identifying known or wanted criminals in a crowd, conducting surveillance in secured areas, and locating missing persons in various scenarios.


Tello Drone Face Tracking
This repository contains code for real-time face tracking using a DJI Tello drone. The drone captures video frames, detects a face, and then uses a PID controller to move itself and keep the face in the center of the frame.

## Features:
1. Real-time face tracking using Haar cascades.
2. Use of PID controllers for smooth and accurate drone movement.
3. Option to save the video feed to an MP4 file.
4. Separate processes for face tracking, video display, and video recording for efficient multitasking.
5. Graceful shutdown on keyboard interrupts.

## Dependencies:
1. cv2: OpenCV library for computer vision tasks.
2. djitellopy: Python interface for DJI Tello drone.
3. imutils: Image processing utility functions.
4. multiprocessing: Standard library for parallel execution of tasks.

## How to Run:
1. Ensure you have all dependencies installed.
2. Clone this repository:

``` bash
git clone <repository_link>
```

   3. Navigate to the repository's directory and run the main script:
``` bash
cd <repository_directory>
python <script_name>.py
```

## Code Overview:
   1. signal_handler: Handles keyboard interrupts to ensure the Tello drone lands safely and any video writers release their resources.
   2. track_face_in_video_feed: The main function responsible for controlling the drone, detecting faces, and using PID controllers to move the drone.
   3. show_video: Displays the video feed in a window using OpenCV.
   4. video_recorder: Saves the video frames to an MP4 file.

The main portion of the code sets up multiprocessing, creating separate processes for the three main tasks and ensuring their coordinated execution.

## Configuration:
There are several parameters you can adjust:

1. TARGET_FACE_SIZE: Target size for the detected face in the video frame.
2. max_speed_limit: Maximum speed that the drone will send as a command.
3. Various PID controller parameters for pan, tilt, and distance.




# Tello Drone Hand Gesture Control
This project integrates MediaPipe's Hand Solutions with the Tello drone to control the drone using hand gestures. Specifically, the gestures supported are "thumbs up" and "thumbs down".

## Features

1. Hand Gesture Detection: Uses MediaPipe's Hand Solutions for detecting hand gestures in real-time.
2. Tello Drone Integration: Connects to the Tello drone's video stream and sends commands based on the detected hand gestures.
3. Thumbs Up Gesture: The drone takes off when this gesture is detected.
4. Thumbs Down Gesture: The drone lands when this gesture is detected.

## Setup

1. Ensure you have Python 3 installed.
2. Install the necessary libraries:
    ``` bash
    pip install cv2 mediapipe djitellopy
    ```
3. Connect your computer to the Tello drone's Wi-Fi network.

## Usage

1. Run the script
   ``` bash
    python3 your_script_name.py
    ```
2. Show a "thumbs up" gesture to the camera to make the drone take off.
3. Show a "thumbs down" gesture to the camera to make the drone land.
4. To exit the program, press 'Esc'.

## Notes

1. Ensure the lighting is adequate for hand detection.
2. There's a 5-second delay between gestures to prevent unintentional repeated commands.
3. Always use this in a spacious and safe environment, ensuring no harm to people or objects around.





# Drone Voice Command Controller
Control your drone using simple voice commands! This script allows users to command a drone using specific voice instructions.

## Features
1. Voice-activated commands for specific drone maneuvers.
2. Uses Google's Speech Recognition for processing audio commands.
3. Provides feedback through print statements to track the command status.

## Pre-requisites
1. Python
OpenCV:
    ``` bash
   pip install opencv-python
   ```
djitellopy: 
   ``` bash
   pip install djitellopy
   ```
SpeechRecognition:
   ``` bash
   pip install SpeechRecognition
   ```
PyAudio: 
   ``` bash
   pip install pyaudio
   ```

## Setup
1. Clone this repository.
2. Navigate to the repository's directory.
3. Install the necessary libraries using pip.
4. Run the script using python.

## How to Use
1. Ensure your drone is connected and its battery level is above 20%.
2. Start the script.
3. Wait for the "Mic recognized" and "We got the audio" messages.
4. Start speaking your commands.

## Supported Voice Commands
1. Flip: Makes the drone flip forward.
2. Apple: Performs a "dance" maneuver by moving the drone up and down.
3. Circle: Makes the drone rotate counter-clockwise and then clockwise.

## Troubleshooting
If you encounter the "Could not understand audio" message, try speaking more clearly or adjusting your microphone settings. If there's an issue connecting to the Speech Recognition service, check your internet connection and the error messages for more details.





