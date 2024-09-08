# Yoga-Pose-Detection

This project is focused on building a **Yoga Pose Detection and Correction System** using **MediaPipe** and **deep learning** techniques. The system is designed to detect yoga poses in real time, classify them, and provide feedback to users to correct their form, making it a useful tool for yoga practitioners and instructors.


## Overview

This project aims to create a real-time yoga pose detection and correction application that runs on a mobile device. It leverages the **MediaPipe** library for pose estimation and uses a **Convolutional Neural Network (CNN)** model trained on custom yoga pose data to classify the poses and suggest corrections.

### Key Objectives:
- Detect yoga poses in real-time using MediaPipe.
- Classify detected poses into predefined categories.
- Provide corrective feedback to improve user form.
- Deploy the model in a mobile application using **Kotlin**.

## Features

- **Real-time Pose Detection**: Uses MediaPipe to detect and track body landmarks.
- **Pose Classification**: Classifies yoga poses based on skeleton data.
- **Pose Correction**: Provides real-time feedback for correcting the user's posture.
- **Mobile Application**: The model is integrated into a mobile app for ease of use.
- **Gamification**: Encourages user engagement with progress tracking and achievements.

## Data Preparation

- The dataset consists of images representing different yoga poses.
- Use MediaPipe to generate landmarks and lines, resulting in images with a black background and white landmarks/lines.
- Store processed images in the `data/processed` directory.

## Model Training

- The model is a Convolutional Neural Network (CNN) trained on the yoga pose dataset.
- The training process involves using skeleton data (landmarks) to classify yoga poses.
- The model is validated using a test dataset to ensure real-time performance.

## Deployment

- The model is integrated into a mobile application using Kotlin.
- The app uses MediaPipe for real-time pose detection and the trained CNN model for classification and correction.

## Results

- The model achieves real-time classification with an accuracy of 94%
- The corrective feedback is evaluated based on user testing and comparison with expert recommendations.

## Future Work

- Enhance the dataset with more poses and variations.
- Improve the feedback mechanism using advanced computer vision techniques.
- Add support for multiple users and group yoga sessions.
- Incorporate additional sensors for more accurate pose detection (e.g., accelerometers).
