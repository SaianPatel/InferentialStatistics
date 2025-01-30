import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# n - Number of Rolls
n = 5000

# Roll the "die" n times
samples = stats.randint(1,7).rvs(n)

# Get the empirical mean of the samples
sampleMean = np.mean(samples)

# Display the result
print(f"\n Empirical mean of {n} dice rolls = {sampleMean:.2f}")

# Usually around 3.5