import scipy.stats as stats
import numpy as np

# Set the number of samples
nSamples = 10000

# Generate the samples
samples = stats.randint(1, 7).rvs(nSamples)

# Count each occurrence
counts = np.bincount(samples)[1:]

# Display the results
print("\nDice Roll Counts:")
for i, count in enumerate(counts, 1):
    print(f"Number {i}: {count}")