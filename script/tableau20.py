from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np

# These are the "Tableau 20" colors as RGB.    
tableau20_int = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229),
             (242, 222, 4)]
tableau20 = [(r / 255., g / 255., b / 255.) for r, g, b in tableau20_int]

tableau_colors = {
  'light_blue': tableau20[18]
  , 'dark_blue': tableau20[0]
  , 'orange': tableau20[2]
  , 'light_orange': tableau20[3]
  , 'red': tableau20[6]
  , 'green': tableau20[4]
  , 'yellow': tableau20[20]
  , 'light_green': tableau20[5]
  , 'purple': tableau20[8]
}

if __name__ == '__main__':
  fig, ax = plt.subplots()
  x = np.arange(0, 5, 0.1);

  #for rank in range(len(tableau20)):
  for i, c in enumerate(tableau20):
      plt.plot(x, i * np.ones(len(x)), lw=2.5, color=c)
  ax.set_ylim([-1, len(tableau20)])


  #plt.show()
  output_file = 'plot/tableu20_colors.pdf'
  plt.savefig(output_file, bbox_inches='tight', format='pdf')
  print('Saved to', output_file)
