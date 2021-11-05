# event frame is just draw events on a figure. 

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
    num_events = 5000
    img = np.zeros(shape=img_size, dtype=int)

    for i in range(num_events):
        img[y[i], x[i]] = (2*p[i]-1)

    # draw image
    fig = plt.figure()
    fig.suptitle('Event Frame')
    plt.imshow(img, cmap='gray')
    plt.xlabel("x [pixels]")
    plt.ylabel("y [pixels]")
    plt.colorbar()
    plt.savefig('event_frame.jpg')
    plt.show()
