#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Hotbox, Spark 
load_times = (5.6309, 32.665)
transform_times = (14.7661, 70.873)
width = 0.35

ind = np.arange(len(load_times))
p1 = plt.bar(ind + width / 2., load_times, width, color='r')
p2 = plt.bar(ind + width / 2., transform_times, width, color='y', bottom=load_times)

plt.ylabel('Time (seconds)', fontsize=20)
plt.title('\n'.join(wrap(
'Ngram Transform Time', 30)), fontsize=20)
plt.xticks(ind + width, ('Hotbox', 'Spark'), size=20)
plt.yticks(size=20)
#plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Loading', 'Transform'), loc=2, fontsize=20)

axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

output_file = 'plot/ngram.png'
plt.savefig(output_file, bbox_inches='tight')
print('Saved to', output_file)
