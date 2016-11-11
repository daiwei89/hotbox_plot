#!/usr/bin/env python
# a bar plot with errorbars
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 2.4))
# fig.subplots_adjust(left=0.2, bottom=0.2)
ax = fig.add_subplot(111)

compute_time = [
2.155,
2.2625,
2.2525

]

comm_time = [
0.2175,
0.035,
0.035

]

compute_time_baseline = [
2.075,
2.14,
2.14

]

comm_time_baseline = [
3.73,
3.275,
3.255

]

compute_time_singletable = [
2.079375,
2.39966275,
2.26976925

]

comm_time_singletable = [
1.65725,
0.22903725,
0.23018325

]

width = 0.6       # the width of the bars
margin = 0.6
N = len(compute_time)
ind = np.arange(N)  # the x locations for the groups
ind2 = []
for i in range(len(ind)):
  ind2.append(ind[i] + len(ind) + margin)
ind3 = []
for i in range(len(ind2)):
  ind3.append(ind2[i] + len(ind2) + margin)
# ind1 = [0, 2, 3]
# ind2 = [1]

# fig, ax = plt.subplots()
rects11 = ax.bar(ind, compute_time, width, color='c', edgecolor='black', hatch='x')
rects12 = ax.bar(ind, comm_time, width, color='red', edgecolor='black', hatch='', bottom=compute_time)
rects21 = ax.bar(ind2, compute_time_singletable, width, color='c', edgecolor='black', hatch='x')
rects22 = ax.bar(ind2, comm_time_singletable, width, color='red', edgecolor='black', hatch='', bottom=compute_time_singletable)
rects31 = ax.bar(ind3, compute_time_baseline, width, color='c', edgecolor='black', hatch='x')
rects32 = ax.bar(ind3, comm_time_baseline, width, color='red', edgecolor='black', hatch='', bottom=compute_time_baseline)

# add some
ax.set_xlim(xmin=-0.2)
ax.set_xticks([ind[1] + width/2, ind2[1] + width/2, ind3[1] + width/2])
ax.set_xlim(xmax=ind3[2] + width + 0.5)
ax.set_xticklabels(('GeePS', 'GeePS-single-table', 'CPU-PS'))
# ax.set_ylabel('Time to process one batch (sec)')
ax.set_ylabel('Time per batch (sec)')
ax.set_ylim(ymax=9.5)
ax.set_yticks([0, 2, 4, 6, 8])

ax.legend((rects12[0], rects11[0]), ('Stall time', 'Computation time'), loc=1,prop={'size':10})

ax.text(rects12[0].get_x()+rects12[0].get_width()/2, rects12[0].get_y()+rects12[0].get_height() + 0.2, 'Slack 0', ha='center', va='bottom', fontsize=9)
ax.text(rects12[1].get_x()+rects12[1].get_width()/2, rects12[1].get_y()+rects12[1].get_height() + 0.2, 'Slack 1', ha='center', va='bottom', fontsize=9)
ax.text(rects12[2].get_x()+rects12[2].get_width()/2, rects12[2].get_y()+rects12[2].get_height() + 0.2, 'Slack Inf', ha='center', va='bottom', fontsize=9)

ax.text(rects22[0].get_x()+rects22[0].get_width()/2, rects22[0].get_y()+rects22[0].get_height() + 0.2, 'Slack 0', ha='center', va='bottom', fontsize=9)
ax.text(rects22[1].get_x()+rects22[1].get_width()/2, rects22[1].get_y()+rects22[1].get_height() + 0.2, 'Slack 1', ha='center', va='bottom', fontsize=9)
ax.text(rects22[2].get_x()+rects22[2].get_width()/2, rects22[2].get_y()+rects22[2].get_height() + 0.2, 'Slack Inf', ha='center', va='bottom', fontsize=9)

ax.text(rects32[0].get_x()+rects32[0].get_width()/2, rects32[0].get_y()+rects32[0].get_height() + 0.2, 'Slack 0', ha='center', va='bottom', fontsize=9)
ax.text(rects32[1].get_x()+rects32[1].get_width()/2, rects32[1].get_y()+rects32[1].get_height() + 0.2, 'Slack 1', ha='center', va='bottom', fontsize=9)
ax.text(rects32[2].get_x()+rects32[2].get_width()/2, rects32[2].get_y()+rects32[2].get_height() + 0.2, 'Slack Inf', ha='center', va='bottom', fontsize=9)

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
plt.savefig('adamnet-compute-comm-times.pdf', bbox_inches='tight')