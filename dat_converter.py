import numpy as np

cms_string_list = ['0.9','2.76','7']
particle_string_list = ['pbar','dbar']

for cms_string in cms_string_list:
    for particle_string in particle_string_list:

        data = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data/ALICE_'+particle_string+'_data_'+cms_string+'.dat').T

        file = open('/mnt/d/Uni/Lectures/thesis/ALICE_data/ALICE_'+particle_string+'_data_'+cms_string+'.txt', 'w')

        for i in range(len(data[0])):
            file.write(str(data[0][i]))
            file.write(' ')
            file.write(str(data[1][i]))
            file.write(' ')
            if(particle_string == 'dbar'):
                file.write(str(data[2][i]))
            file.write('\n')
        file.close()