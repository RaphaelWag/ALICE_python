import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# best levy tsallis fit with mass [2.75991840e-04 1.18458411e+01 3.21585998e-01 8.63896540e-01]
# with bounds p0=[2,5,0.1,2],bounds=(0,100)
def levy_tsallis(pT, N, n, C):
    # m0 = 2 * 0.9382720813  # mass in GeV/c
    m0 = 2
    mT = np.sqrt(pT ** 2 + m0 ** 2)
    term1 = (n - 1.) * (n - 2.)
    term2 = 2 * np.pi * n * C * (n * C + m0 * (n - 2.))
    term3 = 1. + (mT - m0) / (n * C)
    return N * term1 / term2 * (term3 ** (-n))


def hagedorn(pT, b, pT0, N):
    m0 = 2
    return N * pT / np.sqrt(pT ** 2 + m0 ** 2) * (1 + pT / pT0) ** (-b)


fit_function = levy_tsallis

# set cms energy
cms_string = '7'

# READ IN DATA FROM PYTHIA
data_sim = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data_mc/pbar_data_' + cms_string + '.txt').T
data_sim_x = data_sim[0]
data_sim_y = data_sim[1]

# READ IN DATA FROM ALICE
data_alice = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data/ALICE_d_data_' + cms_string + '.dat').T
data_alice_y = data_alice[1]
data_alice_x = data_alice[0]
data_alice_error = data_alice[2]

data_alice_x_f = np.insert(data_alice_x, 0, 0.1)
data_alice_y_f = np.insert(data_alice_y, 0, 4.5 * 10 ** (-5))

# popt, pcov_ = curve_fit(levy_tsallis, data_alice_x_f, data_alice_y_f,method='trf', maxfev=100000, p0=[0.1,0.9,0.5])
# print(popt)
popt, pcov_ = curve_fit(fit_function, xdata=data_alice_x, ydata=data_alice_y, sigma=data_alice_error,method='dogbox', maxfev=1000000,
                        p0=[2.75991840e-04, 1.18458411e+01, 3.21585998e-01], bounds=(0, 100))
print(popt)

full_x_range = np.linspace(0.1, 5, 100)

plt.semilogy(data_alice_x, data_alice_y, 'o', color='red', label='data')
plt.semilogy(full_x_range, fit_function(full_x_range, *popt), color='blue', label='fit')
plt.legend()
plt.savefig('levy_tsallis.jpeg', quality=95, dpi=100)
