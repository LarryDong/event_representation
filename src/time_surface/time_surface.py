# Time surface is also called 'surface of active events'

import numpy as np
from matplotlib import pyplot as plt

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
        if (p[i] > 0):
            sae[y[i], x[i]] = np.exp(-(t_ref-ts[i]) / tau)
        else:
            sae[y[i], x[i]] = -np.exp(-(t_ref-ts[i]) / tau)
        
        ## none-polarity Timesurface
        # sae[y[i], x[i]] = np.exp(-(t_ref-ts[i]) / tau)

    fig = plt.figure()
    fig.suptitle('Time surface')
    plt.imshow(sae, cmap='gray')
    plt.xlabel("x [pixels]")
    plt.ylabel("y [pixels]")
    plt.colorbar()
    plt.savefig('time_surface.jpg')
    plt.show()
