import matplotlib.pyplot as plt
import numpy as np


def get_x_y_bins(filepath):
    file = open(filepath, mode='r')
    x_ = np.asarray(file.readline().split(), dtype=np.float)
    y_ = np.asarray(file.readline().split(), dtype=np.float)
    return x_, y_


cms_string_list = ['0.9', '2.76', '7']
path = '/mnt/d/Uni/Lectures/thesis/results/p_x_corr/scatter2d_'

for cms_string in cms_string_list:
    #    x, y = get_x_y_bins(path + cms_string + '.txt')
    #    X, Y = np.meshgrid(x, np.log10(y))
    data_time = np.loadtxt(path + cms_string + '_time.txt', dtype=np.float).T
    data_space = np.loadtxt(path + cms_string + '_space.txt', dtype=np.float).T
    f, (time, space) = plt.subplots(1, 2, sharex=True, sharey=True)
    time.loglog(data_time[0], data_time[1], 'go', markersize = 0.05)
    space.loglog(data_space[0], data_space[1], 'ro', markersize = 0.05)
    time.set_xlabel('|p_n - p_p|/GeV')
    time.set_ylabel('|x_n - x_p|')
    space.set_xlabel('|p_n - p_p|/GeV')
    f.set_size_inches(10, 5, forward=True)
    plt.savefig('p_x_scatter' + cms_string + '.jpeg', dpi=1000, quality=95)
    plt.clf()
    plt.cla()
    plt.close()
