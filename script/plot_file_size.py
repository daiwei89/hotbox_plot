#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# libsvm, hotbox
libsvm_means = (17.1,0)
hotbox_means = (5.6,0)

N = 2
#colors = ['b', 'y', 'k', 'r', 'g'][:N]

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
offset = 0.35

fig, ax = plt.subplots()
#fig.set_size_inches(18.5, 10.5)
rects = []
rects.append(ax.bar(ind + offset, libsvm_means, width, color='y'))
rects.append(ax.bar(ind + offset + width, hotbox_means, width, color='r'))
#for i, (m, c) in enumerate(zip(means, colors)):
#  rects.append(ax.bar(ind + width * i, m, width, color=c))

# add some text for labels, title and axes ticks
ax.set_ylabel('File Size', fontsize=20)
ax.set_title('File Sizes Comparison', fontsize=20)
ax.set_xticks(ind + (N * width) / 2 + offset)
ax.set_xticklabels(('Higgs',))
#ax.set_ylim([0.5, 0.9])
plt.xticks(size=20)
plt.yticks(size=20)
axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

legend = ax.legend((rects[0][0],rects[1][0]), ('Libsvm', 'Hotbox'), \
  loc='upper right', ncol=1)
legend.get_frame().set_linewidth(2)

#plt.show()
output_file = 'plot/file_sizes.png'
plt.savefig(output_file, bbox_inches='tight')
print('Saved to', output_file)
