import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# for 7TeV deuterons
# best levy tsallis fit with mass [2.75991840e-04 1.18458411e+01 3.21585998e-01 8.63896540e-01]
# with bounds p0=[2,5,0.1,2],bounds=(0,100)

def levy_tsallis(pT, N, n, C):
    m0 = 0.9382720813  # protonmass in GeV/c
    # m0 = 1.87561294257 # deuteronmass in GeV/c
    mT = np.sqrt(pT ** 2 + m0 ** 2)
    term1 = (n - 1.) * (n - 2.)
    term2 = 2 * np.pi * n * C * (n * C + m0 * (n - 2.))
    term3 = 1. + (mT - m0) / (n * C)
    return N * term1 / term2 * (term3 ** (-n))


def hagedorn(pT, b, pT0, N):
    # m0 =  0.9382720813  # protonmass in GeV/c
    m0 = 1.87561294257  # deuteronmass in GeV/c
    return N * pT / np.sqrt(pT ** 2 + m0 ** 2) * (1 + pT / pT0) ** (-b)


fit_function = levy_tsallis

# set cms energy
cms_string = '2.76'
particle_string = 'pbar'

# READ IN DATA FROM ALICE
data_alice = np.loadtxt(
    '/mnt/d/Uni/Lectures/thesis/ALICE_data/ALICE_' + particle_string + '_data_' + cms_string + '.dat').T
data_alice_y = data_alice[1]
data_alice_x = data_alice[0]
#data_alice_error = data_alice[2]

data_alice_x_f = np.insert(data_alice_x, 0, 0.1)
data_alice_y_f = np.insert(data_alice_y, 0, 4.5 * 10 ** (-5))

popt, pcov_ = curve_fit(fit_function, xdata=data_alice_x, ydata=data_alice_y,
                        #sigma=data_alice_error,
                        method='dogbox',
                        maxfev=1000000,
                        p0=[2.75991840e-04, 1.18458411e+01, 3.21585998e-01],
                        bounds=(0, 100))
print(popt)

full_x_range = np.linspace(0.1, 5, 100)

plt.semilogy(data_alice_x, data_alice_y, 'o', color='red', label='data')
plt.semilogy(full_x_range, fit_function(full_x_range, *popt), color='blue', label='fit')
plt.legend()
plt.savefig('levy_tsallis.jpeg', quality=95, dpi=100)

# Fitted soltions
# deuterons
# 7TeV
# [2.67379555e-04 7.17737684e+00 2.16662510e-01]

# protons
# 7TeV
# [0.16786071 6.57842206 0.21988719]

# anti deuterons
# 7TeV
# [2.58556639e-04 6.69472191e+00 2.05455426e-01]
# 2.76 TeV
# [1.82134769e-04 6.32034776e+00 2.01147103e-01]
# 0.9 TeV
# [1.66384712 2.00001457 0.15052795]

# anti protons
# 7TeV
# [0.16840874 6.64441391 0.22235898]
# 2.76 TeV
# [0.14240616 4.64402908 0.17337713]
# 0.9 TeV
# [0.10202219 6.03658744 0.17646152]
