import scipy.stats as stats

# Set mu
mu = 25

# Set sigma
sigma = 5

# Calculate the probability of P(X<=8)
prob = stats.norm.cdf((mu + 2*sigma), mu, sigma) - stats.norm.cdf((mu - 2*sigma), mu, sigma)

# Display the result
print(f"P(mu-2*sigma<=X<=mu+2*sigma) for X~N({mu}, {sigma}) is={prob:.4f}")

# Should be ~95%