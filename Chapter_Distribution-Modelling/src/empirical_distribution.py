
import matplotlib.pyplot as plt
from scipy import stats

sample = [1.0, 2.3, 1.53, 0.5, 0.2]
emp_dist = stats.ecdf(sample)

print(emp_dist)

ax = plt.subplot()
emp_dist.cdf.plot(ax)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'Empirical CDF $\tilde{F}$')
plt.savefig('empirical_distribution_example.svg')
plt.show()
