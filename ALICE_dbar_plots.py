import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#READ IN DATA FROM PYTHIA
data_sim_nw = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data_mc/dbar_data_7_nw.txt').T
data_sim_dw = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data_mc/dbar_data_7_dw.txt').T
data_sim_cw = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data_mc/dbar_data_7_cw.txt').T

data_list = [data_sim_nw,data_sim_dw,data_sim_cw]
color_list = ['g', 'r', 'b']
label_list = ['nw', 'dw', 'cw']
lists = zip(data_list,color_list,label_list)
#READ IN DATA FROM ALICE
data_alice = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data/ALICE_dbar_data_7.dat').T


for data, color, label in lists:
    plt.errorbar(data[0], data[1], yerr=data[2], fmt=color+'o', ecolor=color, capthick=2, label=label)

plt.errorbar(data_alice[0],data_alice[1],yerr=data_alice[2],fmt='yo',ecolor='y',capthick=2, label='ALICE')
plt.yscale('log')
plt.legend()
plt.savefig('/mnt/d/Uni/Lectures/thesis/ALICE_python/dbar_coalescence.jpeg',quality=95,dpi=200)
