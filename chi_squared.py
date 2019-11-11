import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

cms_string_list = {'0.9': '3', '2.76': '7', '7': '20'}
fp = 1
total_bins = 0
chi_squared_total = np.zeros(shape=100)
chi_squared_total_w = np.zeros(shape=100)
chi_squared_x = np.zeros(shape=100)

for cms_string in cms_string_list:
    # READ IN DATA FROM PYTHIA

    norm = int(cms_string_list[cms_string]) - fp
    total_bins += int(cms_string_list[cms_string])

    chi_squared = np.loadtxt(
        '/mnt/d/Uni/Lectures/thesis/ALICE_data/simulated_ALICE_data/chi_squared_' + cms_string +'.txt').T
    chi_squared_y = chi_squared[0]
    chi_squared_x = chi_squared[1]

    chi_squared_mc = np.loadtxt(
        '/mnt/d/Uni/Lectures/thesis/ALICE_data/simulated_ALICE_data/chi_squared_' + cms_string + '_mc' + '.txt').T
    chi_squared_mc_y = chi_squared_mc[0]
    chi_squared_mc_x = chi_squared_mc[1]

    chi_squared_w = np.loadtxt(
        '/mnt/d/Uni/Lectures/thesis/ALICE_data/simulated_ALICE_data/chi_squared_' + cms_string + '_w.txt').T
    chi_squared_w_y = chi_squared_w[0]
    chi_squared_w_x = chi_squared_w[1]

    chi_squared_mc_w = np.loadtxt(
        '/mnt/d/Uni/Lectures/thesis/ALICE_data/simulated_ALICE_data/chi_squared_' + cms_string + '_mc' + '_w.txt').T
    chi_squared_mc_w_y = chi_squared_w[0]
    chi_squared_mc_w_x = chi_squared_w[1]

    plt.plot(chi_squared_x, chi_squared_y / norm, 'yD', markersize=1)
    plt.plot(chi_squared_w_x, chi_squared_w_y / norm, 'rD', markersize=1)
    # plt.plot(chi_squared_mc_x, chi_squared_mc_w_y / norm, 'bo')
    # plt.plot(chi_squared_mc_w_x, chi_squared_mc_w_y / norm, 'go')

    plt.ylabel('chi squared')
    plt.xlabel('p0/GeV')

    pythia = mpatches.Patch(color='y', label='no weigths')
    pythia_weighted = mpatches.Patch(color='r', label='weights')
    plt.legend(handles=[pythia, pythia_weighted])
    plt.savefig('chi_squared_' + cms_string + '.jpeg', dpi=300, quality=95)
    plt.clf()
    plt.cla()
    plt.close()

    chi_squared_total += chi_squared_y
    chi_squared_total_w += chi_squared_w_y

norm = total_bins - fp

plt.plot(chi_squared_x, chi_squared_total / norm, 'yo', markersize=1)
plt.plot(chi_squared_x, chi_squared_total_w / norm, 'ro', markersize=1)
plt.ylabel('chi squared')
plt.xlabel('p0/GeV')
plt.xlim(0.320, 0.360)
plt.ylim(0, 16)

pythia = mpatches.Patch(color='y', label='no weigths')
pythia_weighted = mpatches.Patch(color='r', label='weights')
plt.legend(handles=[pythia, pythia_weighted])
plt.savefig('chi_squared_total.jpeg', dpi=300, quality=95)
plt.clf()
plt.cla()
plt.close()

print(min(chi_squared_total / norm), min(chi_squared_total_w / norm))
