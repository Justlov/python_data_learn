#!/usr/bin/env python3
# encoding = 'utf-8'

import numpy as np

import matplotlib.pyplot as plt
plt.style.use('ggplot')
mu1,mu2,sigma = 100,130,15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
n,bins,patches = ax1.hist(x1,bins=50,normed=False,color='darkgreen')
n,bins,patches = ax1.hist(x2,bins=50,normed=False,color='orange',alpha=0.5)

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('bins')
plt.ylabel('Number of values in Bin')
fig.suptitle("Histogras",fontsize=14,fontweight='bold')
ax1.set_title("Two Fraquency Distributions")
plt.savefig('histogram.png',dpi=400,bbox_inches='tight')