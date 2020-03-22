import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
import imageio
import os

def create_random_list(length):
    l = [i for i in range(1, length+1)]
    shuffle(l)
    return l

def display(l, fname='', curr=-1, next=-1, sorted=None, color1='#b41e2c', color2='#2cb41e', color3='#7f8c8d', x=None, title=''):
    plt.clf()
    if not x:
        x = range(len(l))

    if not len(l) == len(x):
        l = l + [0] * (len(x) - len(l))

    bar_l = plt.bar(x, l, color='#1e77b4')

    if sorted is not None:
        for i in sorted:
            bar_l[i].set_color(color3)

    if curr >= 0:
        bar_l[curr].set_color(color1)

    if next >= 0:
        bar_l[next].set_color(color2)

    axes = plt.gca()
    axes.set_title(title)
    axes.set_ylim([0, 10])
    axes.set_ylabel('Value')
    axes.set_xlabel('Index')

    plt.xticks(np.arange(0, len(l)+1, 1))
    plt.yticks(np.arange(0, len(l)+1, 1))
    plt.draw()
    plt.savefig(fname)

def display_match(l, fname, match, *iter):
    plt.clf()
    axes = plt.gca()
    axes.set_ylim([0, 10])
    axes.set_ylabel("Value")
    axes.set_xlabel("Index")

    plt.xticks(np.arange(0, len(l)+1, 1))
    plt.yticks(np.arange(0, len(l)+1, 1))

    if match:
        bar_l = plt.bar(range(len(l)), l, color="#1e77b4")
        bar_l[iter[0]].set_color("#b41e2c")
        bar_l[iter[1]].set_color("#2cb41e")
        plt.draw()
        plt.savefig(fname)
    else:
        bar_l = plt.bar(range(len(l)), l, color='#1e77b4')
        bar_l[iter[0]].set_color("#7f8c8d")
        bar_l[iter[1]].set_color("#7f8c8d")
        plt.draw()
        plt.savefig(fname)

def make_gif(k, fname='sorting.gif', fps=1):
    images = []
    filenames = [(str(i)+'.png') for i in range(k)]
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(fname, images, fps=fps)
    for filename in filenames:
        os.remove(filename)