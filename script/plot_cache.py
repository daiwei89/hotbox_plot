#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
from tableau20 import *

output_file = 'plot/cache_time.pdf'

# tf, ngram
normal_means = (94.5368, 42.92113333)
cache_out_means = (102.823, 99.8619)
cache_in_means = (18.0473, 90.53963333)
#spark_means = (200, 150, 200)

#hotbox_std = (1.23, 0)

# # of entries in each mean, or number of clusters.
N = 2
#num_clusters = 2
#colors = ['b', 'y', 'k', 'r', 'g'][:N]

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
offset = 0.35
tick_offset = 0.1

fig, ax = plt.subplots()
#fig.set_size_inches(18.5, 10.5)
rects = []
rects.append(ax.bar(ind + offset, normal_means, width, \
  color=tableau_colors['green']))
rects.append(ax.bar(ind + offset + width, cache_out_means, width, \
  color=tableau_colors['yellow']))
rects.append(ax.bar(ind + offset + 2 * width, cache_in_means, width, \
  color=tableau_colors['light_blue']))
#for i, (m, c) in enumerate(zip(means, colors)):
#  rects.append(ax.bar(ind + width * i, m, width, color=c))

# add some text for labels, title and axes ticks
ax.set_ylabel('Time (seconds)', fontsize=20)
#ax.set_title('File Sizes Comparison', fontsize=20)
ax.set_xticks(ind + (N * width) / N + offset + tick_offset)
ax.set_xticklabels(('DNN\nTransform', 'CP'))
ax.set_ylim([0, 140])
plt.xticks(size=20)
plt.yticks(size=20)
axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

legend = ax.legend((rects[0][0], rects[1][0], rects[2][0]), \
  ('No cache', 'Load+cache out', 'Load from cache'), \
  loc='upper right', ncol=1)
legend.get_frame().set_linewidth(2)

#plt.show()
plt.savefig(output_file, bbox_inches='tight', format="pdf")
print('Saved to', output_file)

