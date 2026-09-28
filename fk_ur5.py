"""Forward kinematics of a UR5 arm using the product of exponentials.

Given six joint angles (radians), prints the 4x4 pose of the end-effector
so I can compare it with what CoppeliaSim shows.
"""
import numpy as np
import modern_robotics as mr  # pip install modern_robotics

# UR5 dimensions in metres
W1, W2, L1, L2, H1, H2 = 0.109, 0.082, 0.425, 0.392, 0.089, 0.095

# End-effector pose when all joints are at zero
M = np.array([[-1, 0, 0, L1 + L2],
              [ 0, 0, 1, W1 + W2],
              [ 0, 1, 0, H1 - H2],
              [ 0, 0, 0, 1]])

# Screw axes in the space frame, one column per joint
Slist = np.array([[0, 0,  1,  0,       0,       0],
                  [0, 1,  0, -H1,      0,       0],
                  [0, 1,  0, -H1,      0,       L1],
                  [0, 1,  0, -H1,      0,       L1 + L2],
                  [0, 0, -1, -W1,      L1 + L2, 0],
                  [0, 1,  0,  H2 - H1, 0,       L1 + L2]]).T

thetas = [0.7854, -0.7854, 0.7854, -1.5708, -1.5708, 0.7854]

T = mr.FKinSpace(M, Slist, thetas)
print("End-effector pose T:")
print(np.round(T, 4))
print("Position (x, y, z) in metres:", np.round(T[:3, 3], 3))
