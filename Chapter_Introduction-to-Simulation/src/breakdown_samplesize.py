#!/usr/bin/env python3
#

# Synopsis: Code estimating E[N] for the sum-of-uniforms breakdown
# problem as a function of sample size n.

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

nSamples=100000
step=100 # We only visualize the average for every 100 steps.

sampleArray = np.zeros(nSamples)

def SampleX() :
    n = 0
    sum = 0.0
    while True :
        sum += uniform.rvs()
        n+=1
        if sum >= 1.0 :
            break
    return n

sampleArray = [SampleX() for i in range(nSamples)]

nSubSamples = int(nSamples / step)
subSampleArray = np.zeros(nSubSamples)
indexArray = np.zeros(nSubSamples)

# Create estimates as a function of number of samples in increments of 'step':

for i in range(0, nSubSamples) :
    indexArray[i] = step * (i+1)
    subSampleArray[i] = np.average( sampleArray[0:(step * (i+1))] )

# This gives the estimate:
print( subSampleArray[-1] )

# Now plot the evolution:
fig, ax = plt.subplots(1, 1)
ax.plot(indexArray, subSampleArray, 'b-', lw=1, alpha=0.6, label=r'$\hat{E}[N](n)$')
ax.legend(loc='best', frameon=False)
plt.xlabel(r'$n$')
plt.savefig('system_breakdown_n.svg')
plt.show()
