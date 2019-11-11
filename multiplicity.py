import matplotlib.pyplot as plt
import numpy as np

file = '/mnt/d/Uni/Lectures/thesis/ALICE_multiplicity/charged_particle_distribution_7000.txt'

pdf = np.loadtxt(file)
inverse_eta = 1 / 4.3

# plot multiplicity distribution
x_axis = [n * inverse_eta for n in range(len(pdf))]
plt.semilogy(x_axis, pdf)
plt.xlim(0, 50)
plt.xlabel('Nch/eta')
plt.ylabel('pdf')
plt.savefig('multiplicity_pdf_7.jpeg', dpi=100, quality=95)
plt.clf()
plt.cla()
plt.close()

cdf = np.cumsum(pdf)
plt.plot(x_axis, cdf)
plt.xlim(0, 50)
plt.xlabel('Nch/eta')
plt.ylabel('cdf')
plt.savefig('multiplicity_cdf_7.jpeg', dpi=100, quality=95)

# find bins for multiplicity classes
limits = [0.62, 0.19, 0.095, 0.048, 0.047]
climits = np.cumsum(limits)
bin_limits = [0]
index_limits = [0]
j = 0
for i in range(len(cdf)):
    if (not cdf[i] > climits[j]): continue
    bin_limits = np.append(bin_limits, i * inverse_eta)
    index_limits = np.append(index_limits, i)
    j += 1
    if (j >= len(limits)): break
bin_limits = np.append(bin_limits, len(cdf) * inverse_eta)
index_limits = np.append(index_limits, len(cdf))

print('bin limits', bin_limits)
print('index limits', index_limits)

# calculate average number of charged particles in each class
for i in range(len(index_limits) - 1):
    integration_range = np.asarray(range(index_limits[i], index_limits[i + 1]))
    # mean value = integral x*p(x)*dx
    # p(x) = pdf
    x = integration_range * inverse_eta
    # pdf*x
    # renormalize pdf
    pdf_ = pdf[integration_range] / np.sum(pdf[integration_range])
    pdf_x = pdf_ * x
    print('Class', i+1,np.sum(pdf_x))
integration_range = np.asarray(range(index_limits[0], index_limits[-1]))
# mean value = integral x*p(x)*dx
# p(x) = pdf
x = integration_range * inverse_eta
# pdf*x
# renormalize pdf
pdf_ = pdf[integration_range] / np.sum(pdf[integration_range])
pdf_x = pdf_ * x
print('Class', 'total',np.sum(pdf_x))
