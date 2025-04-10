# KalmanFilterExtraPerception
Kalman Filter for Fusing Pose Estimates with Reflection Handling

This script uses a Kalman filter to combine pose estimates from two cameras, while addressing potential inaccuracies caused by reflective surfaces like sheet metal. The Kalman filter helps improve the accuracy of the pose estimate by accounting for discrepancies between the two camera measurements.

Features
	•	Initializes a Kalman filter with a state vector for 3D position and orientation.
	•	Fuses pose data from two cameras using averaging and Kalman filter predictions.
	•	Adjusts confidence in measurements based on the difference between the two camera poses, particularly useful for dealing with reflective surfaces.
	•	Optionally incorporates historical data to refine the pose estimate.

Requirements
	•	Python 3.x
	•	Numpy
	•	FilterPy

How It Works
	1.	Initialization: The Kalman filter is initialized with specific parameters suited for 3D pose estimation.
	2.	Fusion of Pose Estimates: The script takes the pose data from two cameras, averages them, and adjusts the confidence based on reflection thresholds. If historical data is available, it is used to refine the estimates.
	3.	Reflection Handling: Discrepancies between the two cameras’ measurements are detected. If the difference exceeds a set threshold, the confidence in those particular measurements is reduced to mitigate the effects of reflections.

Usage
	•	Initialize the Kalman filter.
	•	Provide two sets of pose data (one from each camera).
	•	Optionally include historical data for improved accuracy.
	•	The script will output the fused pose estimate.

Tuning Parameters
	•	Reflection Threshold: Defines the maximum allowed difference between corresponding pose elements before confidence is reduced.
	•	Confidence Weights: Used to adjust the weight of each pose element based on the reflection threshold.

Output

The output is the fused pose estimate, which is a more accurate representation of the object’s position and orientation, factoring in the measurements from both cameras and any historical data.
