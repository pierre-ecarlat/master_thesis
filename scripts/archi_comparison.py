#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


# data
nb_architectures = 5
names = ['LeNet\n(1998)', 'AlexNet\n(2012)', 'VGGNet\n(2014)', 'GoogleNet\n(2014)', 'ResNet\n(2015)']
depth = [3, 5, 16, 22, 152]
nb_param = [0.43, 60, 138, 6.8, 2.3]
top5 = [47, 15.3, 7.5, 6.67, 3.57]

# design
width = 5

# plot
abc = np.arange(nb_architectures)
abc = (abc+1)*(2*width) - width

f, axarr = plt.subplots(2, sharex=True)

axarr[0].set_xticks(abc)
axarr[0].set_xticklabels(names, fontsize=14)

axarr[0].bar(abc - width, depth, 2*width, color='b', alpha=0.5, linewidth=0)
axarr[0].set_ylabel('Depth of networks', color='b', fontsize=14)
for tl in axarr[0].get_yticklabels():
    tl.set_color('b')

tmpAx = axarr[0].twinx()
tmpAx.bar(abc - width/2, top5, width, color='r')
tmpAx.set_ylabel('Error rate (%)', color='r', fontsize=14)
for tl in tmpAx.get_yticklabels():
    tl.set_color('r')
for i, txt in enumerate(top5):
    tmpAx.annotate(txt, (abc[i]-1.5+1, top5[i]-3), size=10)

axarr[1].plot(abc, nb_param, marker='o')
axarr[1].set_ylabel('Number of parameters\n(millions)', fontsize=14)
for i, txt in enumerate(nb_param):
    axarr[1].annotate(txt, (abc[i]-1.5, nb_param[i]+4), size=14)
axarr[1].set_ylim(0, max(nb_param)+20)

plt.text(57, 25, '(a)', fontsize=14,
         horizontalalignment='center',
         verticalalignment='center')

plt.text(57, -35, '(b)', fontsize=14,
         horizontalalignment='center',
         verticalalignment='center')

plt.show()
