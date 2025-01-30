import scipy.stats as stats

# n - Number of trials - 15 items
n = 15

# p - Probability of Success (i.e. getting a defective item) - 0.08
p = 0.08

# k - Value of interest (i.e. number of successes) - at most 2 defective items
# At most 2 defective items is P(X<=2)
k = 2

# Calculate the probability
prob = stats.binom.cdf(k, n, p)

# Display the result
print(f"P(X<=2): {prob:.4f}")

# For n = 15, p = 0.08, k = 2 - P(X<=2)= 0.8870.