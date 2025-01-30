import scipy.stats as stats
import matplotlib.pyplot as plt

# n - Number of trials
n = 8

# p - Probability of Success
p = 0.4

# nSamples - Number of samples
nSamples = 2000

# Generate the samples
samples = stats.binom.rvs(n, p, size=nSamples)

# Plot results
plt.hist(samples, bins=range(n+2), density=True, edgecolor='black')
plt.title("Binomial Sampling (n=8, p=0.4, nSamples=2000)")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")
plt.show()