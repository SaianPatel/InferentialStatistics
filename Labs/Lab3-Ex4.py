import scipy.stats as stats

# Set the bounds of the uniform distribution
a, b = 0, 20

# Create the uniform distribution
uniform = stats.uniform(loc=a, scale=b-a)

# Calculate the probability of P(3<=X<=7)
prob = uniform.cdf(4)-uniform.cdf(16)

# Display the result
print(f"P(4<=X<=16)={prob:.4f}")

# P(4<=X<=16) for X~U(0,20) is 0.6