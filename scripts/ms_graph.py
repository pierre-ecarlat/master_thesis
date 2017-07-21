#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


# data
nb_cycles = 3
nb_datasets = 2
datasets_names = ['oku', 'swi']

# osselait
#data_oku = [26.03, 31.1, 31.36, 32.42, 33.87, 35.31]
#data_swi = [26.35, 66.43, 33.57, 67.31, 36.95, 68.35]

# kicklee
#data_oku = [67.33, 39.40, 67.36, 33.87, 66.86, 50.31]
#data_swi = [31.17, 68.41, 50.85, 69.47, 55.94, 69.62]

# otaria
data_oku = [73.47, 48.57, 73.52, 68.60, 73.88, 72.18] # last = res frm both instead of 47.0
data_swi = [38.68, 66.85, 50.85, 68.31, 55.41, 68.87]

data_average = [(data_oku[i] + data_swi[i])/2. for i in range(6)]

# plot
plt.plot(data_oku, 'bo-', label="Validation on Okutama")
plt.plot(data_swi, 'go-', label="Validation on Swiss")
plt.plot(data_average, 'r--', label="Average")
#plt.plot(data_mix, 'ro-')
#plt.plot(data_oku, data_swi, 'bo--')

plt.legend()

plt.xlabel('Trained on')
plt.ylabel('Mean IU (%)')
#plt.xlabel('mean IU (%) on Swiss validation set')
#plt.ylabel('mean IU (%) on Okutama validation set')
#plt.xlim([min(data_oku)-5,max(data_oku)+5])
plt.ylim([min(data_swi)-5,max(data_swi)+20])

all_names = datasets_names
for _ in range(nb_cycles-1):
    all_names += datasets_names
plt.xticks(range(6), all_names)

plt.show()
