import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

n,p = 10, 0.5
x = np.arange(0, n+1)
pmf = stats.binom.pmf(x, n, p)

plt.bar(x, pmf, color='skyblue', edgecolor='black')
plt.title("Binomial PMF (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()