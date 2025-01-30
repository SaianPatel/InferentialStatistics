import scipy.stats as stats

# Set mu
mu = 10

# Set sigma
sigma = 3

# Calculate the probability of P(X<=8)
prob = stats.norm.pdf(8, mu, sigma)

# Display the result
print(f"PDF at x=8 is={prob:.4f}")

# 0.1065