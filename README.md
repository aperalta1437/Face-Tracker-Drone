# Drone_Vision
MCCC 111B Final Project utilizing OpenCV and Ardupilot

Project Description:

This project utilizes the pyardrone and openCV libraries to create a simple drone control system that tracks a and follows a single human face, positioning the drone to keep the tracked object in the center of its field of view.

Files:

- drone_face_tracking.py: Runs an autonomous drone functionality that immediately launches the drone and begins reacting to a recognised face. The displayed viewport can be closed by pressing 'q' and will land the drone.
- drone_ui.py: Provides a very simple ui for manual drone control, primarily for testing and debugging purposes. This file does not use the drone's camer at all.
