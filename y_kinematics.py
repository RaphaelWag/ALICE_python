import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.8, 0.8, 34)
X, Y = np.meshgrid(x, x)
nd = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_results/y_kinematics/y_nd.txt', skiprows=2)

plt.contourf(X, Y, nd, 100)
plt.savefig('test.jpeg')
