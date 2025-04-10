import numpy as np
from filterpy.kalman import KalmanFilter

def initialize_kalman():
    kf = KalmanFilter(dim_x=6, dim_z=6)  
    
    kf.F = np.eye(6)
    
    kf.H = np.eye(6)
    
    kf.P *= 1e3  
    kf.R *= 1e1 
    kf.Q *= 1e-2
    
    return kf

def fuse_pose_estimates(kf, pose_cam1, pose_cam2, historical_data=None):
    # Simple averaging for initial fused measurement
    measurement = (np.array(pose_cam1) + np.array(pose_cam2)) / 2
    
    if historical_data:
        historical_avg = np.mean(historical_data, axis=0)
        measurement = 0.7 * measurement + 0.3 * historical_avg 
    
    reflection_threshold = 0.1  
    confidence_weights = np.ones(6)
    
    for i in range(6):
        if abs(pose_cam1[i] - pose_cam2[i]) > reflection_threshold:
            confidence_weights[i] = 0.5 
    
    measurement = confidence_weights * measurement + (1 - confidence_weights) * kf.x 
    
    kf.predict()
    kf.update(measurement)
    
    return kf.x 

kf = initialize_kalman()
pose_cam1 = [0.5, 1.2, 0.8, 0.1, 0.05, 0.02] 
pose_cam2 = [0.6, 1.1, 0.85, 0.12, 0.04, 0.01]  
historical_data = [
    [0.55, 1.15, 0.82, 0.11, 0.06, 0.015],
    [0.53, 1.13, 0.79, 0.09, 0.04, 0.02]  
]

fused_pose = fuse_pose_estimates(kf, pose_cam1, pose_cam2, historical_data)
print("Fused Pose Estimate:", fused_pose)
