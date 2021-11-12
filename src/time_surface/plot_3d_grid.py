# plot time-surface in a 3d grid format.

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape

def extract_data(filename):
    infile = open(filename, 'r')
    ts, x, y, p = [], [], [], []
    for line in infile:
        words = line.split()
        ts.append(float(words[0]))
        x.append(int(words[1]))
        y.append(int(words[2]))
        p.append(int(words[3]))
    infile.close()
    return ts, x, y, p


if __name__ == '__main__':

    ts, x, y, p = extract_data('../../data/slider_seg.txt')

    img_size = (180,240)
    img = np.zeros(shape=img_size, dtype=int)

    # parameters for Time Surface
    t_ref = ts[-1]      # 'current' time
    tau = 50e-3         # 50ms

    sae = np.zeros(img_size, np.float32)
    # calculate timesurface using expotential decay
    for i in range(len(ts)):
        if(p[i] == 0):          # only for negative ts.
            sae[y[i], x[i]] = np.exp(-(t_ref-ts[i]) / tau)
    
    # select a roi, to avoid to much data.
    roi_x0 = 120
    roi_x1 = 140
    roi_y0 = 40
    roi_y1 = 60
    x_range = np.arange(roi_x0, roi_x1)
    y_range = np.arange(roi_y0, roi_y1)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xx, yy = np.meshgrid(x_range, y_range)
    x, y = xx.ravel(), yy.ravel()
    
    top = sae[roi_y0:roi_y1, roi_x0:roi_x1].ravel()
    colors = plt.cm.jet(top/np.max(top))                # color coding
    bottom = np.zeros_like(top)

    ax.bar3d(x, y, bottom, 1, 1, top, shade=True, color=colors)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('time-surface 3d grid')
    plt.show()
