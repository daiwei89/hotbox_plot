#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from textwrap import wrap
import pandas as pd
import sys
from tableau20 import *

select_scale_file = 'data/select_scale.dat'
spark_select_scale_file = 'data/spark_select_scale.dat'
#output_file = 'plot/select_scale.pdf'
ngram_scale_file = 'data/ngram_scale.dat'
#output_file = 'plot/ngram_scale.pdf'
normalize_scale_file = 'data/normalize_scale.dat'
spark_normalize_scale_file = 'data/spark_normalize_scale.dat'
#output_file = 'plot/normalize_scale.pdf'
output_file = 'plot/all_scale_spark.pdf'

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

# Read spark
df = pd.read_csv(spark_select_scale_file, sep=' ', header=0)
speeds = df.as_matrix()
all_speeds_spark = np.zeros((speeds.shape[0], 4))
all_speeds_spark[:,:2] = speeds[:,:2]

df = pd.read_csv(spark_normalize_scale_file, sep=' ', header=0)
speeds = df.as_matrix()
all_speeds_spark[:,3] = speeds[:,1]

font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 16}

#lines = plt.plot(speeds[:,0], speeds[:,1], 'bo-', label="Hotbox")
#lines = plt.errorbar(speeds[:,0], speeds[:,1], yerr=speeds[:,2], fmt='bo-',
#        label="SystemX")

fig, ax = plt.subplots(1, 2, sharey=True, figsize=(10,8))
lines = []
lines.append(ax[0].plot(all_speeds[:,0], all_speeds[:,1], 'o-', 
  color=tableau_colors['green']))
lines.append(ax[0].plot(all_speeds[:,0], all_speeds[:,2], '.-', 
  color=tableau_colors['red']))
lines.append(ax[0].plot(all_speeds[:,0], all_speeds[:,3], '--',
  color=tableau_colors['dark_blue']))
lines.append(ax[0].plot(all_speeds[:,0], all_speeds[:,0], 'k:'))
plt.sca(ax[0])
for line in lines:
  plt.setp(line, linewidth=2)

plt.xticks(size=20)
plt.yticks(size=20)
plt.xlabel('Number of Workers', fontsize=20)
plt.ylabel('Speed-up', fontsize=20)

axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

# Spark scalability
lines = []
lines.append(ax[1].plot(all_speeds_spark[:,0], all_speeds_spark[:,1], 'o-', 
  color=tableau_colors['green']))
lines.append(ax[1].plot(all_speeds_spark[:,0], all_speeds_spark[:,2], '.-', 
  color=tableau_colors['red']))
lines.append(ax[1].plot(all_speeds_spark[:,0], all_speeds_spark[:,3], '--',
  color=tableau_colors['dark_blue']))
lines.append(ax[1].plot(all_speeds_spark[:,0], all_speeds_spark[:,0], 'k:'))
plt.sca(ax[1])
for line in lines:
  plt.setp(line, linewidth=2)

plt.xticks(size=20)
plt.yticks(size=20)
plt.xlabel('Number of Workers', fontsize=20)
#plt.ylabel('Speed-up', fontsize=20)

axes = plt.gca()
for axis in ['top','bottom','left','right']:
  axes.spines[axis].set_linewidth(2)

fig.legend((lines[0][0], lines[1][0], lines[2][0], lines[3][0]), ('Load', 'CP', \
  'Normalize', 'Ideal'), 'upper center', mode='expand', ncol=4, fontsize=20, \
  borderaxespad=0, columnspacing=-20)

"""
plt.subplot(121)
lines = plt.plot(all_speeds[:,0], all_speeds[:,1], 'o-', 
  color=tableau_colors['green'], label="Load")
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,2], '.-', 
  color=tableau_colors['red'], label="CP")
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,3], '--',
  color=tableau_colors['dark_blue'], label="Normalize")
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,0], 'k:', label="Ideal")
plt.setp(lines, linewidth=2)
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=2, mode="expand", borderaxespad=0.)
plt.legend(bbox_to_anchor=(0.5, -0.05), loc='upper center',
           ncol=4, mode="expand", borderaxespad=0.)

plt.subplot(122)
lines = plt.plot(all_speeds[:,0], all_speeds[:,1], 'o-', 
  color=tableau_colors['green'])
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,2], '.-', 
  color=tableau_colors['red'])
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,3], '--',
  color=tableau_colors['dark_blue'])
#lines = plt.errorbar(all_speeds[:,0], all_speeds[:,3], fmt='bo-',
#        label="Normalize")
plt.setp(lines, linewidth=2)
# ideal speedup
lines = plt.plot(all_speeds[:,0], all_speeds[:,0], 'k:')
plt.setp(lines, linewidth=2)

#plt.figure(num=None, figsize=(1,1.5))
#fig = plt.Figure(figsize=(20, 3))
fig, ax = plt.subplots(121, sharex=True, figsize=(10,6))

plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label="test2")
# Place a legend above this subplot, expanding itself to
# fully use the given bounding box.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

#ax0 = fig.add_subplot(gs[0])
#ax[1] = fig.add_subplot(gs[1])
lines = plt.plot(all_speeds[:,0], all_speeds[:,1], 'o-', 
  color=tableau_colors['green'], label="Load")
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,2], '.-', 
  color=tableau_colors['red'], label="CP")
plt.setp(lines, linewidth=2)
lines = plt.plot(all_speeds[:,0], all_speeds[:,3], '--',
  color=tableau_colors['dark_blue'], label="Normalize")
#lines = plt.errorbar(all_speeds[:,0], all_speeds[:,3], fmt='bo-',
#        label="Normalize")
plt.setp(lines, linewidth=2)
# ideal speedup
lines = plt.plot(all_speeds[:,0], all_speeds[:,0], 'k:', label="Ideal")

ax[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=4)

#plt.sca(ax0)
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

# Plot spark.
lines = ax[1].plot(all_speeds_spark[:,0], all_speeds[:,1], 'o-', 
  color=tableau_colors['green'])
plt.setp(lines, linewidth=2)
lines = ax[1].plot(all_speeds_spark[:,0], all_speeds[:,2], '.-', 
  color=tableau_colors['red'])
plt.setp(lines, linewidth=2)
lines = ax[1].plot(all_speeds_spark[:,0], all_speeds[:,3], '--',
  color=tableau_colors['dark_blue'])
plt.setp(lines, linewidth=2)
# ideal speedup
lines = ax[1].plot(all_speeds[:,0], all_speeds[:,0], 'k:')
"""

#plt.sca(ax[1])


plt.legend(loc=2, fontsize=20)
plt.savefig(output_file, bbox_inches='tight', format='pdf')
print('Saved to', output_file)
