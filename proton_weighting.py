import numpy as np

# set cms energy
cms_string = '2.76'

# READ IN DATA FROM PYTHIA
data_sim = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data_mc/pbar_data_'+cms_string+'.txt').T
data_sim_x = data_sim[0]
data_sim_y = data_sim[1]

# READ IN DATA FROM ALICE
data_alice = np.loadtxt('/mnt/d/Uni/Lectures/thesis/ALICE_data/ALICE_pbar_data_'+cms_string+'.dat').T
data_alice_y = data_alice[1]

N_points = len(data_sim_x)
weights = (data_alice_y/data_sim_y)

file = open('/mnt/d/Uni/Lectures/thesis/ALICE_weighting/discrete_weights/weights_pbar_'+cms_string+'.txt', 'w')

file.write(str(N_points))
file.write('\n')

for i in range(N_points):
    file.write(str(data_sim_x[i]))
    file.write(' ')
    file.write(str(weights[i]))
    file.write('\n')
file.close()
