#!/usr/bin/env python3
#
# Synopsis: Code for the breakdown problem, part 2c. This is about
# estimating the probability that the system breaks down prior the
# expected time to failure. Here we have used the output from the
# previous code to get the range for tau and the corresponding
# expected value.
#

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import uniform

mpl.rcParams['text.usetex'] = True
# mpl.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

a = 0.1
b = 0.3

def TimeToFailure(tau_c) :
    k = 1

    # Initialize k = 1
    Y_k = uniform.rvs()
    if Y_k >= 1 :
        return k

    while True :
        k += 1

        if Y_k < tau_c :
            Y_k += uniform.rvs()
            if Y_k >= 1 :
#                print("a")
                return k
        else :
            R_k = uniform.rvs(loc=a, scale=(b-a))
            X_k = uniform.rvs()
            Y_k = max(0, Y_k - R_k) + X_k
            if Y_k >= 1.0 :
#                print("b")
                return k

# nSamples=100000
# tau_range = np.arange(0.0, 1.0, 0.05)
# exp_range = [ np.average( [TimeToFailure(tau) for i in range(nSamples)]) for tau in tau_range]

# Saved from previous Python code for 2b using nSamples = 100000

tau_range = [ 0., 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
              0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]

exp_range = [3.50089, 3.50116, 3.48066, 3.45451, 3.40618, 3.37466,
             3.3197, 3.27293, 3.21661, 3.17628, 3.11639, 3.0729,
             3.02904, 2.98762 , 2.9485, 2.89767, 2.8611, 2.81905,
             2.78328, 2.74615]

pairs = zip(tau_range, exp_range)

nSamples=10000
indicator_prob = [ np.average( [0.0 if TimeToFailure(v[0]) < v[1] else 1.0
                                for i in range(nSamples)]) for v in pairs]

# Now plot the estimated probability as a function of tau_c
fig, ax = plt.subplots(1, 1)
ax.plot(tau_range, indicator_prob, 'b-', lw=1, alpha=0.6)
plt.title(r'Probability of failure prior to expected failure time as a function of $\tau_c$')
plt.xlabel(r'$\tau_c$')
plt.savefig('system-breakdown-2c.svg')
plt.show()
