#!/usr/bin/env python3
#
# Synopsis: Code estimating E[N] for the sum-of-uniforms breakdown
#   problem using a vectorized solution.

import numpy as np
from scipy.stats import uniform
import multiprocessing

nSamples=100000

def SampleX(x) :
    n = 0
    sum = 0.0
    while True :
        sum += uniform.rvs()
        n+=1
        if sum >= 1.0 :
            break
    return n

vec_SampleX = np.vectorize(SampleX)
#sampleArray = vec_SampleX(np.zeros(nSamples))

iput = np.zeros(nSamples)
sampleArray = SampleX(iput)

print(np.average(sampleArray))
