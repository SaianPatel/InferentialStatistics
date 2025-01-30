import scipy.stats as stats

# Set mu
mu = 12

# Set sigma
sigma = 4

# Calculate the probability of P(X<=8)
prob = stats.norm.cdf(15, mu, sigma)

# Display the result
print(f"P(X<=15) for X~N({mu}, {sigma}) is={prob:.4f}")

# 0.7734