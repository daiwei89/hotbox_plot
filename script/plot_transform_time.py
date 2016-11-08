#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
from tableau20 import *

output_file = 'plot/runtime.pdf'

# select, ngram, normalize
hotbox_means = (100.07, 120.8266667, 121.057)
spark_means = (424.272, 0, 739.573)

#hotbox_std = (1.23, 0)

# # of entries in each mean, or number of clusters.
N = 3
#colors = ['b', 'y', 'k', 'r', 'g'][:N]

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
offset = 0.35
tick_offset = -0.1

fig, ax = plt.subplots()
#fig.set_size_inches(18.5, 10.5)
rects = []
rects.append(ax.bar(ind + offset, spark_means, width, \
  color=tableau_colors['green']))
rects.append(ax.bar(ind + offset + width, hotbox_means, width, \
  color=tableau_colors['yellow']))
#for i, (m, c) in enumerate(zip(means, colors)):
#  rects.append(ax.bar(ind + width * i, m, width, color=c))

# add some text for labels, title and axes ticks
ax.set_ylabel('Time (seconds)', fontsize=20)
#ax.set_title('File Sizes Comparison', fontsize=20)
ax.set_xticks(ind + (N * width) / 2 + offset + tick_offset)
ax.set_xticklabels(('Load', 'CP', 'Normalization'))
ax.set_ylim([0, 1000])
plt.xticks(size=20)
plt.yticks(size=20)
axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

legend = ax.legend((rects[0][0],rects[1][0]), ('Spark', 'SystemX'), \
  loc='upper right', ncol=1)
legend.get_frame().set_linewidth(2)

#plt.show()
plt.savefig(output_file, bbox_inches='tight', format="pdf")
print('Saved to', output_file)
