import matplotlib.pyplot as plt
import numpy as np

cms_string_list = {'0.9': '3', '2.76': '7', '7': '20'}
fp = 1
total_bins = 0
chi_squared_total = np.zeros(shape=65)
chi_squared_total_dw = np.zeros(shape=65)
chi_squared_total_cw = np.zeros(shape=65)
chi_squared_nw_x = np.zeros(shape=65)

folder = '/mnt/d/Uni/Lectures/thesis/ALICE_results/chi_squared'

for cms_string in cms_string_list:
    # READ IN DATA FROM PYTHIA

    norm = int(cms_string_list[cms_string]) - fp
    total_bins += int(cms_string_list[cms_string])

    chi_squared_nw = np.loadtxt(folder + '/chi_squared_' + cms_string + '_nw.txt').T
    chi_squared_nw_y = chi_squared_nw[0]
    chi_squared_nw_x = chi_squared_nw[1]

    chi_squared_dw = np.loadtxt(folder + '/chi_squared_' + cms_string + '_dw.txt').T
    chi_squared_dw_y = chi_squared_dw[0]
    chi_squared_dw_x = chi_squared_dw[1]

    chi_squared_cw = np.loadtxt(folder + '/chi_squared_' + cms_string + '_cw.txt').T
    chi_squared_cw_y = chi_squared_cw[0]
    chi_squared_cw_x = chi_squared_cw[1]

    plt.semilogy(chi_squared_nw_x, chi_squared_nw_y / norm, 'yD', markersize=1, label='nw')
    plt.semilogy(chi_squared_dw_x, chi_squared_dw_y / norm, 'rD', markersize=1, label='dw')
    plt.semilogy(chi_squared_cw_x, chi_squared_cw_y / norm, 'bo', markersize=1, label='cw')
    plt.legend()

    plt.ylabel('chi squared')
    plt.xlabel('p0/GeV')

    plt.savefig('chi_squared_' + cms_string + '.jpeg', dpi=300, quality=95)
    plt.clf()
    plt.cla()
    plt.close()

    chi_squared_total += chi_squared_nw_y
    chi_squared_total_dw += chi_squared_dw_y
    chi_squared_total_cw += chi_squared_cw_y

norm = total_bins - fp

plt.semilogy(chi_squared_nw_x, chi_squared_total / norm, 'yo', markersize=1, label='nw')
plt.semilogy(chi_squared_nw_x, chi_squared_total_dw / norm, 'ro', markersize=1, label='dw')
plt.semilogy(chi_squared_nw_x, chi_squared_total_cw / norm, 'bo', markersize=1, label='cw')
plt.ylabel('chi squared')
plt.xlabel('p0/GeV')
# plt.xlim(190, 0.360)
# plt.ylim(0, 16)

plt.legend()
plt.savefig('chi_squared_total.jpeg', dpi=300, quality=95)
plt.clf()
plt.cla()
plt.close()

print(min(chi_squared_total / norm), min(chi_squared_total_dw / norm), min(chi_squared_total_cw / norm))
