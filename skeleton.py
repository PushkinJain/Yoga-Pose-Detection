import cv2
import mediapipe as mp
import numpy as np
import os

# Initialize MediaPipe Pose.
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils  # Utility to draw landmarks and connections
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

# Input and output folder paths
input_folder = 'C:\\Users\\Santosh\\Desktop\\fyp\\DATASET\\TEST\\tree'
output_folder = 'C:\\Users\\Santosh\\Desktop\\fyp\\src\\output_pic_withline\\test\\tree'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # Read the image
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape

        # Convert the image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and find the pose
        result = pose.process(image_rgb)

        # Create a blank numpy array with zeros
        skeleton_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

        # Draw the skeleton on the blank image
        if result.pose_landmarks:
            mp_drawing.draw_landmarks(
                skeleton_image, 
                result.pose_landmarks, 
                mp_pose.POSE_CONNECTIONS,  # This connects the keypoints to form the skeleton
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=5, circle_radius=5),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)
            )

        # Save the image with the skeleton
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, skeleton_image)

print("Processing complete.")
