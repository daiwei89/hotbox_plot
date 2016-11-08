#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import pandas as pd
import sys

#scale_file = 'data/select_scale.dat'
#output_file = 'plot/select_scale.pdf'
#scale_file = 'data/ngram_scale.dat'
#output_file = 'plot/ngram_scale.pdf'
scale_file = 'data/normalize_scale.dat'
output_file = 'plot/normalize_scale.pdf'


df = pd.read_csv(scale_file, sep=' ', header=0)
speeds = df.as_matrix()

font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 16}

#lines = plt.plot(speeds[:,0], speeds[:,1], 'bo-', label="Hotbox")
#lines = plt.errorbar(speeds[:,0], speeds[:,1], yerr=speeds[:,2], fmt='bo-',
#        label="SystemX")
lines = plt.errorbar(speeds[:,0], speeds[:,1], fmt='bo-',
        label="SystemX")
plt.setp(lines, linewidth=2)
# ideal speedup
lines = plt.plot(speeds[:,0], speeds[:,0], 'k--', label="Ideal")
plt.setp(lines, linewidth=2)

plt.xlabel('Number of Workers', fontsize=20)
plt.ylabel('Speed-up', fontsize=20)

axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)
#plt.tick_params(axis='both', which='major', labelsize=10)
#axes.set_xlim([-0.1,0.6])
plt.xticks(size=20)
plt.yticks(size=20)
#axes.set_ylim([ymin,ymax])
#plt.title('\n'.join(wrap(
#'Data Loading Speed-up', 30)), fontsize=20)
plt.legend(loc=2, fontsize=20)
plt.savefig(output_file, bbox_inches='tight', format='pdf')
print('Saved to', output_file)
