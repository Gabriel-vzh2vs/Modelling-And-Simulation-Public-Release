#!/usr/bin/env python3
#

import argparse
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
from scipy.stats import t, skew, kurtosis

# from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

#
# Author: Henning S. Mortveit
#
# Date: 21 Dec 2024
#
# Synopsis: basis analysis related to the Buffon's Needle
#   experiment. Here the needle toss result is captured through the
#   position x in [0, d) of the leftmost (and lower if parallel with
#   the lines) part of the needle and the angle theta of the needle
#   relative to the horizontal line. The length of the needle is l and
#   the distance between adjancent slats is d.
#
#   We regard x as the uniform random variable U[0,d) and theta as the
#   uniform random variable U[-pi/2, pi/2).
#
# The indicator random variable I = I_Intersect recording
# intersections is defined by:

def I_Intersect(x, theta, l, d) :
    return 1.0 if x + l * math.cos(theta) > d else 0.0
#
# The probability that this indicator variable is 1 equals (2l)/(pi d)
# which also equals its expectation E(I). Below, we pick l/d = 1/2,
# leading to the probability of being 1 equaling 1/pi.
#
# The variance of I equals E(I) [1 - E[I]], which for l/d = 1/2
# becomes Var(I) = 1/pi(1-1/pi).
#
# The random variable variable X_n being the average of n independent
# copies of I, X_n = 1/n \sum_{i=k}^n I_k has expectation E(X_n) =
# 1/pi and Var(X_n) = 1/n E(I)[1-E(I)] = (1/n) 1/pi [1 - 1/pi] := s^2.
#

# To read about pseudo-random number generation in Python, see
# https://docs.python.org/3/library/random.html and the reference
#
# M. Matsumoto and T. Nishimura, "Mersenne Twister: A
# 623-dimensionally equidistributed uniform pseudorandom number
# generator", ACM Transactions on Modeling and Computer Simulation
# Vol. 8, No. 1, January pp.3–30 1998.

# N = 1000000000 # 3.141605742553703
# seed_value = 47653


def main() :

    plt.rcParams["text.usetex"] = True

    parser = argparse.ArgumentParser(
        description='Monto Carlo method applied to simulation of Buffon\'s needle')
    parser.add_argument('--N', default=100, type=int, metavar='int',
                        help='number of trials to perform')
    parser.add_argument('--step', default=1, type=int, metavar='int',
                        help='stepsize to use for estimates')
    parser.add_argument('--seed', default=1234, type=int, metavar='int',
                        help='random seed')
    args = parser.parse_args()

    N = args.N
    step = args.step
    seed_value = args.seed

    d = 2.0
    l = 1.0

    pi_half = math.pi / 2.0

    # seed_value = 476531
    # seed_value_0 = 47653

    random.seed(seed_value)

    # Adjusting N, if necessary, to be a multiple of step:

    nMeasurements = int(N / step)
    if nMeasurements*step < N :
        nMeasurements = nMeasurements + 1
        N = step * nMeasurements
        print(f'Adjusted values: N {N}')
    print(f'Step: {step} Measurements: {nMeasurements}')

    # Initialize array of length N with all zeros, then apply the MC
    # method N times:

    sample_array = np.zeros(shape=(N), dtype=np.float64)

    for i in range(0, N) :
        x = random.uniform(0, d)
        theta = random.uniform(-pi_half, pi_half)
        sample_array[i] = I_Intersect(x, theta, l, d)

    # Output analysis

    skw = skew(sample_array)
    krt = kurtosis(sample_array)

    index_array = np.zeros(shape=(nMeasurements), dtype=np.int64)

    xbar = np.zeros(shape=index_array.shape, dtype=np.float64)
    sample_var = np.zeros(shape=index_array.shape, dtype=np.float64)
    var_xbar = np.zeros(shape=index_array.shape, dtype=np.float64)
    pi_average = np.zeros(shape=index_array.shape, dtype=np.float64)
    half_length = np.zeros(shape=index_array.shape, dtype=np.float64)
    std_xbar = np.zeros(shape=index_array.shape, dtype=np.float64)

    alpha = 0.05
    mIdx = 0

    for i in range(0, len(sample_array), step) :
        index_array[mIdx] = i+step
        xbar[mIdx] = np.average( sample_array[0:i+step] )
        sample_var[mIdx] = np.var( sample_array[0:i+step], ddof=1)
        var_xbar[mIdx] = sample_var[mIdx] / np.float64(i+step)
        std_xbar[mIdx] = math.sqrt(var_xbar[mIdx])
        half_length[mIdx] = t.ppf(1.0-alpha, i+step-1, loc=0.0, scale=1.0 ) * math.sqrt(var_xbar[mIdx])
        mIdx = mIdx + 1

    pi_average = 1/xbar

    print(f'Final report: ')
    print(f'  Sample size, alpha: {N} {alpha}')
    print(f'  Skewness estimate: {skw}')
    print(f'  Kurtosis estimate: {krt}')
    print(f'  Estimate for pi(N): {pi_average[nMeasurements-1]}')
    print(f'  Estimate for variance of X: {sample_var[nMeasurements-1]}')
    print(f'  Estimate for std. dev. of X: {math.sqrt(sample_var[nMeasurements-1])}')
    print(f'  Estimate for variance of X(N): {var_xbar[nMeasurements-1]}')
    print(f'  Estimate for std. dev. of X(N): {math.sqrt(var_xbar[-1])}')
    print(f'  Half-length: {half_length[nMeasurements-1]}')
    print(f'  CI: [{pi_average[nMeasurements-1]-half_length[nMeasurements-1]}, {pi_average[nMeasurements-1]+half_length[nMeasurements-1]}]')

    fig, (axis1, axis2) = plt.subplots(2, figsize=(16, 9))

    fig.subplots_adjust(left=0.035, right=0.995, top=0.9, bottom=0.1)
    _ = [spine.set_edgecolor('black') for spine in plt.gca().spines.values()]
    # _ = [spine.set_linewidth(2) for spine in plt.gca().spines.values()]

    # for spine in plt.gca().spines.values():
    #     spine.set_edgecolor('black')
    #     spine.set_linewidth(2)

    pi_const_array = math.pi * np.ones(shape=index_array.shape, dtype=np.float64)


    axis1.plot(index_array, pi_average, label=r"MC estimate $\hat\pi$  " + f"(seed: {seed_value})")
    axis1.plot(index_array, pi_const_array, label=r"$\pi$")
    axis1.set_ylim(2.5, 3.5)
    axis1.legend(loc="lower right")
    axis1.xaxis.set_major_locator(MaxNLocator(integer=True))

    axis1.title.set_text(r"MC estimation for $\pi$ using Buffon's needle experiment Using the \texttt{random} library of Python  " + f"({sys.version})")


    # plt.errorbar(step_array, pi_average, sample_std)
    axis2.plot(index_array, var_xbar, label=r"MC: estimate for ${var}[\bar{X}]$: $S^2(n)/n$ " +  f"(seed: {seed_value})")
    axis2.plot(index_array, half_length, label=r"MC: half-length estimate $t_{n-1,1-\alpha/2} \sqrt{S^2(n)/n}$" )
    axis2.plot(index_array, sample_var, label=r"MC: sample variance estimate $\sigma^2$ for X" )
    axis2.plot(index_array, np.sqrt(sample_var), label=r"MC: sample std. dev. estimate $\sigma$ for X" )
    axis2.set_ylim(0, 0.5)
    axis2.xaxis.set_major_locator(MaxNLocator(integer=True))
    axis2.legend(loc="lower right")
    axis2.set_title(r"Sample standard deviation as a function of $n$ for Buffon's needle experiment", y=-0.2, pad=-0)

    plt.show()

    # print(sample_std)

    est =  sum(sample_array) / float(N);

    print(1.0/est)



    return 0



main()
