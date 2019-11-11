import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#READ IN DATA FROM PYTHIA
data_sim = np.loadtxt('D:/Uni/Lectures/thesis/ALICE_data/simulated_ALICE_data/dbar_data_7.txt').T
data_sim_x = data_sim[0]
data_sim_y = data_sim[1]
data_error = data_sim[2]

data_sim_scaled = np.loadtxt('D:/Uni/Lectures/thesis/ALICE_data/simulated_ALICE_data/dbar_data_7_w.txt').T
data_sim_scaled_x = data_sim_scaled[0]
data_sim_scaled_y = data_sim_scaled[1]
scaled_error = data_sim_scaled[2]

#READ IN DATA FROM ALICE
data_alice = np.loadtxt('D:/Uni/Lectures/thesis/ALICE_data/ALICE_dbar_data_7.dat').T


plt.errorbar(data_sim_x,data_sim_y,yerr=data_error,fmt='yD',ecolor='y',capthick=2)
plt.errorbar(data_sim_scaled_x,data_sim_scaled_y,yerr=scaled_error,fmt='rs',ecolor='r',capthick=2)
plt.errorbar(data_alice[0],data_alice[1],yerr=data_error,fmt='bo',ecolor='b',capthick=2)
plt.yscale('log')
alice = mpatches.Patch(color='b', label='ALICE')
pythia = mpatches.Patch(color='y', label='PYTHIA p0=195MeV')
pythia_scaled = mpatches.Patch(color='r', label='PYTHIA scaled p0=203MeV')
plt.legend(handles=[alice,pythia,pythia_scaled])
plt.show()
