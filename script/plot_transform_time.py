#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
from tableau20 import *

output_file = 'plot/runtime.pdf'

# select, ngram, normalize, standardized
hotbox_means = (100.07, 120.8266667, 121.057, 195.125 )
spark_means = (424.272, 900, 739.573, 0)

# TODO(wdai) replace 2472 with real number.
hotbox_means_1node = (1483.996667, 1789.923333, 1534.256667, 1501)
spark_means_1node = (5035.887, 11000, 9925.748, 0)

#hotbox_std = (1.23, 0)

# # of entries in each mean, or number of clusters.
N = 4
#colors = ['b', 'y', 'k', 'r', 'g'][:N]

ind = np.arange(N)  # the x locations for the groups
width = 0.3       # the width of the bars
offset = 0 #0.35
tick_offset = 0.3 #-0.1

fig, ax = plt.subplots(2, sharex=True)
#fig.set_size_inches(18.5, 10.5)
rects = []
rects.append(ax[0].bar(ind + offset, spark_means, width, \
  color=tableau_colors['green']))
rects.append(ax[0].bar(ind + offset + width, hotbox_means, width, \
  color=tableau_colors['yellow']))
#for i, (m, c) in enumerate(zip(means, colors)):
#  rects.append(ax.bar(ind + width * i, m, width, color=c))

# add some text for labels, title and axes ticks
ax[0].set_ylabel('Time (seconds)', fontsize=20)
#ax.set_title('File Sizes Comparison', fontsize=20)
ax[0].set_xticks(ind + (2 * width) / 2 + offset + tick_offset)
ax[0].set_xticklabels(('Load', 'CP', 'Normalize', 'Standardize'))
ax[0].set_ylim([0, 1200])
plt.sca(ax[0])
plt.xticks(size=20)
plt.yticks(size=20)
axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

legend = ax[0].legend((rects[0][0],rects[1][0]), ('Spark', 'SystemX'), \
  loc='upper left', ncol=1)
legend.get_frame().set_linewidth(2)

# Bottom subplot
rects = []
rects.append(ax[1].bar(ind + offset, spark_means_1node, width, \
  color=tableau_colors['green']))
rects.append(ax[1].bar(ind + offset + width, hotbox_means_1node, width, \
  color=tableau_colors['yellow']))
#for i, (m, c) in enumerate(zip(means, colors)):
#  rects.append(ax.bar(ind + width * i, m, width, color=c))

# add some text for labels, title and axes ticks
ax[1].set_ylabel('Time (seconds)', fontsize=20)
#ax.set_title('File Sizes Comparison', fontsize=20)
#ax[1].set_xticks(ind + (N * width) / 2 + offset + tick_offset)
ax[1].set_xticks(ind + tick_offset)
ax[1].set_xticklabels(('Load', 'CP', 'Normalize', 'Standardize'))
ax[1].set_ylim([0, 13000])
plt.sca(ax[1])
plt.xticks(size=20)
plt.yticks(size=20)
axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

#plt.show()
plt.savefig(output_file, bbox_inches='tight', format="pdf")
print('Saved to', output_file)
