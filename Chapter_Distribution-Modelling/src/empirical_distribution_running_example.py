import sys
import matplotlib.pyplot as plt
from scipy import stats


sample = [
    4.875, 5.74, 10.149, 6.197, 11.357, 3.9048, 8.07, 8.055,
    7.067, 9.737, 4.3757, 6.451, 13.023, 10.513, 6.978, 3.7117, 6.919,
    11.466, 7.338, 12.409, 4.4195, 6.729, 4.2673, 14.4, 11.214, 7.777,
    19.62, 3.9662, 4.154, 5.586, 7.619, 5.009, 25.05, 15.58, 7.171,
    6.534, 4.888, 7.841, 5.192, 3.52463, 6.46, 8.074, 17.82, 6.677,
    14.22, 10.826, 7.343, 4.2477, 7.067, 3.6041, 6.675, 11.254, 6.385,
    5.32, 6.44, 9.429, 6.303, 25.78, 8.152, 14.02, 6.199, 10.185,
    7.446, 4.689, 25.74, 6.621, 7.157, 6.158, 7.01, 3.8648, 7.492,
    4.1367, 11.988, 4.4746, 4.838, 5.829, 11.613, 15.36, 5.073, 17.51,
    11.151, 9.558, 4.949, 9.332, 4.4172, 8.342, 19.47, 3.6985, 17.9,
    4.4053, 8.112, 8.617, 7.575, 3.9138, 4.4023, 5.279, 4.4784, 5.007,
    22.66, 5.847
]

emp_dist = stats.ecdf(sample)

# You should inspect the object:
print(emp_dist)

# Use matplotlib to visualize:
ax = plt.subplot()
emp_dist.cdf.plot(ax)

# r-strings permit LaTeX formatting. This is optional, but looks professional.
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'Empirical CDF $\tilde{F}$ of the running example')
plt.savefig('../Figs/empirical_distribution_example_running_example.svg')
plt.show()

# Histograms using various bin counts:

for bin_count in [5, 10, 15, 20, 30] :

    f, axes = plt.subplots(ncols=2, nrows=1,  sharey=False, sharex=False)
    f.set_size_inches(10.0, 2.5)

    axes[0].hist(sample, bins=bin_count, color='lightgray', edgecolor='black')
    axes[0].set_xlabel(r'$x$')
    axes[0].set_title(f'Histogram ($n={bin_count}$)')
    axes[0].set_xlim(left=0, right=30)
    axes[0].set_ylim(bottom=0, top=max(sample))

    axes[1].hist(sample, bins=bin_count, color='lightgray', edgecolor='black', density=True)
    axes[1].set_xlabel(r'$x$')
    axes[1].set_title(f'Normalized ($n={bin_count}$)')
    axes[1].set_xlim(left=0, right=30)
    axes[1].set_ylim(bottom=0, top=1)

    plt.savefig(f'../Figs/histogram_n_{bin_count}_example_running_example.svg')
    plt.show()

sys.exit(0)


f, axes = plt.subplots(ncols=2, nrows=1,  sharey=False)
f.set_size_inches(10.0, 2.5)

# n = 5
axes[0].hist(sample, bins=5, color='lightgray', edgecolor='black')
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Histogram ($n=5$)')
axes[0].set_xlim(left=0, right=30)
axes[0].set_ylim(bottom=0, top=max(sample))

axes[1].hist(sample, bins=5, color='lightgray', edgecolor='black', density=True)
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Normalized ($n=5$)')
axes[1].set_xlim(left=0, right=30)
axes[1].set_ylim(bottom=0, top=1)

plt.savefig('../Figs/histogram_n_5_example_running_example.svg')
plt.show()

# n = 10

f, axes = plt.subplots(ncols=2, nrows=1,  sharey=False)
f.set_size_inches(10.0, 2.5)

axes[0].hist(sample, bins=10, color='lightgray', edgecolor='black')
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Histogram ($n=10$)')
axes[0].set_xlim(left=0, right=30)
axes[0].set_ylim(bottom=0, top=max(sample))

axes[1].hist(sample, bins=10, color='lightgray', edgecolor='black', density=True)
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Normalized ($n=10$)')
axes[1].set_xlim(left=0, right=30)
axes[1].set_ylim(bottom=0, top=1)

plt.savefig('../Figs/histogram_n_10_example_running_example.svg')
plt.show()

# n = 15

f, axes = plt.subplots(ncols=2, nrows=1,  sharey=False)
f.set_size_inches(10.0, 2.5)

axes[0].hist(sample, bins=15, color='lightgray', edgecolor='black')
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Histogram ($n=15$)')
axes[0].set_xlim(left=0, right=30)
axes[0].set_ylim(bottom=0, top=max(sample))

axes[1].hist(sample, bins=15, color='lightgray', edgecolor='black', density=True)
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Normalized ($n=15$)')
axes[1].set_xlim(left=0, right=30)
axes[1].set_ylim(bottom=0, top=1)

plt.savefig('../Figs/histogram_n_15_example_running_example.svg')
plt.show()

# n = 20

f, axes = plt.subplots(ncols=2, nrows=1,  sharey=False)
f.set_size_inches(10.0, 2.5)

axes[0].hist(sample, bins=20, color='lightgray', edgecolor='black')
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Histogram ($n=20$)')
axes[0].set_xlim(left=0, right=30)
axes[0].set_ylim(bottom=0, top=max(sample))

axes[1].hist(sample, bins=20, color='lightgray', edgecolor='black', density=True)
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Normalized ($n=20$)')
axes[1].set_xlim(left=0, right=30)
axes[1].set_ylim(bottom=0, top=1)

plt.savefig('../Figs/histogram_n_20_example_running_example.svg')
plt.show()

# n = 30

f, axes = plt.subplots(ncols=2, nrows=1,  sharey=False)
f.set_size_inches(10.0, 2.5)

axes[0].hist(sample, bins=30, color='lightgray', edgecolor='black')
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Histogram ($n=30$)')
axes[0].set_xlim(left=0, right=30)
axes[0].set_ylim(bottom=0, top=max(sample))

axes[1].hist(sample, bins=30, color='lightgray', edgecolor='black', density=True)
axes[0].set_xlabel(r'$x$')
axes[0].set_ylabel(r'Normalized ($n=30$)')
axes[1].set_xlim(left=0, right=30)
axes[1].set_ylim(bottom=0, top=1)

plt.savefig('../Figs/histogram_n_30_example_running_example.svg')
plt.show()
