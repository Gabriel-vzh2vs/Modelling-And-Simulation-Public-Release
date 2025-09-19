#!/usr/bin/env python3
#
# Synopsis: Code estimating E[N] for the sum-of-uniforms breakdown
#   problem

import numpy as np
from scipy.stats import uniform

nSamples=100000
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

print(np.average(sampleArray))
