#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
from tableau20 import *

#plt.rcdefaults()
fig = plt.figure(figsize=(8, 6))
# fig.subplots_adjust(left=0.2, bottom=0.2)
ax = fig.add_subplot(111)

output_file = 'plot/cache_space.pdf'

objects = ('DNN', 'CP', 'Normalize', 'Bucketize')
offset = 0.3
width = 0.25       # the width of the bars
y_pos = np.arange(len(objects)) + offset
vals = (159, 25580.61, 12207, 2182)

barlist = ax.bar(y_pos, vals, width, align='center',
color=tableau_colors['light_blue'])
#barlist[1].set_color(tableau_colors['yellow'])
#barlist[1].set_edgecolor("black")
#barlist[2].set_color(tableau_colors['light_blue'])
#barlist[2].set_edgecolor("black")
#barlist[3].set_color(tableau_colors['red'])
#barlist[3].set_edgecolor("black")
plt.xticks(y_pos, objects)
plt.xticks(size=20)
plt.yticks(size=20)
plt.ylabel('Cache Size (MBs)', fontsize=20)
axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

"""
N = 2
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
ax.set_ylabel('Run time (seconds)', fontsize=20)
#ax.set_title('File Sizes Comparison', fontsize=20)
ax.set_xticks(ind + (N * width) / 2 + offset + tick_offset)
ax.set_xticklabels(('Load', 'CP', 'Normalization'))
ax.set_ylim([0, 220])
plt.xticks(size=20)
plt.yticks(size=20)
axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

legend = ax.legend((rects[0][0],rects[1][0]), ('Spark', 'SystemX'), \
  loc='upper right', ncol=1)
legend.get_frame().set_linewidth(2)
"""

#plt.show()
plt.savefig(output_file, bbox_inches='tight', format="pdf")
print('Saved to', output_file)
