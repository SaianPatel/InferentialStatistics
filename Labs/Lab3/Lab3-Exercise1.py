import scipy.stats as stats

# n - Number of trials - 12 coin flips
n = 12

# p - Probability of Success (i.e. getting Heads) - 0.5 for a fair coin
p = 0.5

# k - Value of interest (i.e. number of successes) - 5 Heads
k = 5

# Calculate the probability
prob = stats.binom.pmf(k, n, p)

# Display the result
print(f"P(X=5): {prob:.4f}")

# For n = 12, p = 0.5, k = 5 - prob is 0.1934.