#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import pandas as pd
import sys
from tableau20 import *

select_scale_file = 'data/select_scale.dat'
#output_file = 'plot/select_scale.pdf'
ngram_scale_file = 'data/ngram_scale.dat'
#output_file = 'plot/ngram_scale.pdf'
normalize_scale_file = 'data/normalize_scale.dat'
#output_file = 'plot/normalize_scale.pdf'
output_file = 'plot/all_scale.pdf'

df = pd.read_csv(select_scale_file, sep=' ', header=0)
speeds = df.as_matrix()

# 4 for ideal + 3 scalability.
all_speeds = np.zeros((speeds.shape[0], 4))
all_speeds[:,:2] = speeds[:,:2]

df = pd.read_csv(ngram_scale_file, sep=' ', header=0)
speeds = df.as_matrix()
all_speeds[:,2] = speeds[:,1]

df = pd.read_csv(normalize_scale_file, sep=' ', header=0)
speeds = df.as_matrix()
all_speeds[:,3] = speeds[:,1]

font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 16}

#lines = plt.plot(speeds[:,0], speeds[:,1], 'bo-', label="Hotbox")
#lines = plt.errorbar(speeds[:,0], speeds[:,1], yerr=speeds[:,2], fmt='bo-',
#        label="SystemX")
lines = plt.plot(all_speeds[:,0], all_speeds[:,1], 'o-', color=tableau_colors['green'],
        label="Load")
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,2], '.-', color=tableau_colors['red'],
        label="CP")
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,3], '--',
  color=tableau_colors['dark_blue'], label="Normalize")
#lines = plt.errorbar(all_speeds[:,0], all_speeds[:,3], fmt='bo-',
#        label="Normalize")
plt.setp(lines, linewidth=2)
# ideal speedup
lines = plt.plot(all_speeds[:,0], all_speeds[:,0], 'k:', label="Ideal")
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
