import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Set the limits of the uniform distribution
a, b = 0, 10
xU = np.linspace(a, b, 100)
pdfU = stats.uniform(a, b).pdf(xU)

# Set mu and sigma for the Gaussian
mu, sigma = 5, 2
xG = np.linspace(-5, 15, 100)
pdfG = stats.norm(mu, sigma).pdf(xG)

plt.plot(xU, pdfU, label="Uniform (0-10)")
plt.plot(xG, pdfG, label="Gaussian (mu=5, sigma=2)")
plt.title("Uniform vs Gaussian")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()