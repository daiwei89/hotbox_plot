#!/usr/bin/env python
# a bar plot with errorbars
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from tableau20 import *

fig = plt.figure(figsize=(6, 4))
# fig.subplots_adjust(left=0.2, bottom=0.2)
ax = fig.add_subplot(111)

ingest_time_8 = [
3042, # baseline ingest
3042, # baseline ingest
60   # hotbox ingest
]

trans_time_8 = [
110,      # Single thread read
33.025,      # Spark read
43.96      # hotbox read
]

ingest_time_1 = [
3042,
3042,
60
]

trans_time_1 = [
813.75,
146.4,
302.5
]

width = 0.6       # the width of the bars
margin = 0.6
N = len(ingest_time_8)
ind = np.arange(N)  # the x locations for the groups
ind2 = []
for i in range(len(ind)):
  ind2.append(ind[i] + len(ind) + margin)
#ind3 = []
#for i in range(len(ind2)):
#  ind3.append(ind2[i] + len(ind2) + margin)
# ind1 = [0, 2, 3]
# ind2 = [1]

# fig, ax = plt.subplots()
rects11 = ax.bar(ind, ingest_time_1, width, color=tableau_colors['yellow'], edgecolor='black', hatch='x')
rects12 = ax.bar(ind, trans_time_1, width, color=tableau_colors['light_blue'], edgecolor='black', hatch='', \
  bottom=ingest_time_1)
rects21 = ax.bar(ind2, ingest_time_8, width, color=tableau_colors['yellow'], edgecolor='black', hatch='x')
rects22 = ax.bar(ind2, trans_time_8, width, color=tableau_colors['light_blue'], edgecolor='black', hatch='', \
  bottom=ingest_time_8)
#rects31 = ax.bar(ind3, compute_time_baseline, width, color='c', edgecolor='black', hatch='x')
#rects32 = ax.bar(ind3, comm_time_baseline, width, color='red', edgecolor='black', hatch='', bottom=compute_time_baseline)

# add some
ax.set_xlim(xmin=-0.2)
ax.set_xticks([ind[1] + width/2, ind2[1] + width/2])
ax.set_xlim(xmax=ind2[2] + width + 0.5)
ax.set_xticklabels(('1 Nodes', '8 Nodes'))
# ax.set_ylabel('Time to process one batch (sec)')
ax.set_ylabel('Time (seconds)')
ax.set_ylim(ymax=4000)
#ax.set_yticks([0, 2, 4, 6, 8])

ax.legend((rects11[0], rects12[0]), ('Preparation Time', 'Load Time'), loc=1,prop={'size':10})

ax.text(rects12[0].get_x()+rects12[0].get_width()/2, rects12[0].get_y()+rects12[0].get_height() + 0.2, 'Naive Read', ha='center', va='bottom', fontsize=9)
ax.text(rects12[1].get_x()+rects12[1].get_width()/2, rects12[1].get_y()+rects12[1].get_height() + 0.2, 'Spark', ha='center', va='bottom', fontsize=9)
ax.text(rects12[2].get_x()+rects12[2].get_width()/2, rects12[2].get_y()+rects12[2].get_height() + 0.2, 'SystemX', ha='center', va='bottom', fontsize=9)

ax.text(rects22[0].get_x()+rects22[0].get_width()/2, rects22[0].get_y()+rects22[0].get_height() + 0.2, 'Naive Read', ha='center', va='bottom', fontsize=9)
ax.text(rects22[1].get_x()+rects22[1].get_width()/2, rects22[1].get_y()+rects22[1].get_height() + 0.2, 'Spark', ha='center', va='bottom', fontsize=9)
ax.text(rects22[2].get_x()+rects22[2].get_width()/2, rects22[2].get_y()+rects22[2].get_height() + 0.2, 'SystemX', ha='center', va='bottom', fontsize=9)

#ax.text(rects32[0].get_x()+rects32[0].get_width()/2, rects32[0].get_y()+rects32[0].get_height() + 0.2, 'Slack 0', ha='center', va='bottom', fontsize=9)
#ax.text(rects32[1].get_x()+rects32[1].get_width()/2, rects32[1].get_y()+rects32[1].get_height() + 0.2, 'Slack 1', ha='center', va='bottom', fontsize=9)
#ax.text(rects32[2].get_x()+rects32[2].get_width()/2, rects32[2].get_y()+rects32[2].get_height() + 0.2, 'Slack Inf', ha='center', va='bottom', fontsize=9)

def autolabel(rectss):
    # attach some text labels
    n = len(rectss)
    for j in range(len(rectss[0])):
      height = 0
      for i in range(n):
        height = height + rectss[i][j].get_height()
      ax.text(rectss[0][j].get_x()+rectss[0][j].get_width()/2, height + 0.6, '%0.0f'% height,
            ha='center', va='bottom', fontsize=8)

# autolabel([rects1, rects12, rects3])
# autolabel([rects12, rects122, rects32])

plt.tight_layout()
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

# plt.show()
plt.savefig('plot/tf_time.pdf', bbox_inches='tight')
