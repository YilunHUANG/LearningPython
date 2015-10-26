# Section 1.2.6 Bayesian curve fitting
# Section 3.3.1 Parameter distribution
# Section 3.3.2 Predictive distribution

import numpy as np
import matplotlib.pyplot as plt

# the number of training data
N = 10
# the number of model parameters
M = 10

# regularization parameter
alpha = 0.005
beta = 11.1

# domain
X_MIN = 0.0
X_MAX = 1.0
# codomain
T_MIN = -1.5
T_MAX = 1.5

# linear model (3.2)
def y(x, w):
    return np.dot(w, phi(x))

def phi(x):
    # polynomial basis function
    def polynomial_basis_function(j):
        return x**j
    
    # Gaussian basis function (3.4)
    def gaussian_basis_function(j, s = 0.1):
        # dummy
        if j == 0:
            return 1
        else:
            mu_j = (X_MAX - X_MIN) / (M - 2) * j
            return np.exp(-(x - mu_j)**2 / (2 * s**2))
    
    # sigmoidal basis fuction (3.5)
    def sigmoidal_basis_function(j, s = 0.1):
        # logistic sigmoid function (3.6)
        def sigma(a):
            return 1 / (1 + np.exp(-a))
        
        # dummy
        if j == 0:
            return 1
        else:
            mu_j = (X_MAX - X_MIN) / (M - 2) * j
            return sigma((x - mu_j) / s)
    
    return np.array([polynomial_basis_function(j) for j in range(M)])

# Bayesian estimation
def estimate(x_train, t_train):
    # design matrix (3.16)
    PHI = np.array([phi(x_train[n]) for n in range(N)])
    
    # variance of posterior probability distribution (3.54)
    S_INV = alpha * np.identity(M) + beta * PHI.T.dot(PHI)
    # inverse matrix of S
    S = np.linalg.inv(S_INV)
    
    # means of posterior probability distribution (3.53)
    m = beta * S.dot(PHI.T).dot(t_train)
    
    return {"m": m, "S": S}

def main():
    # sine curve
    x_ideal = np.linspace(X_MIN, X_MAX, 1000)
    t_ideal = np.sin(2 * np.pi * x_ideal)
    
    # training data with Gaussian noise of variance 0.09
    x_train = np.linspace(X_MIN, X_MAX, N)
    loc = 0.0
    scale = 0.3
    t_train = np.sin(2 * np.pi * x_train) + np.random.normal(loc, scale, N)
    
    # estimate
    params = estimate(x_train, t_train)
    
    # mean of predictive distribution
    t_mean = np.array([y(x, params["m"]) for x in x_ideal])
    
    # variance of predictive distribution
    variance = np.array([1.0 / beta + phi(x).T.dot(params["S"]).dot(phi(x)) for x in x_ideal])
    # standard devitation
    sigma = np.sqrt(variance)
    t_upper = t_mean + sigma
    t_lower = t_mean - sigma
    
    # figure
    plt.plot(x_ideal, t_ideal, "g-")
    plt.plot(x_ideal, t_mean, "r-")
    plt.fill_between(x_ideal, t_upper, t_lower, color = "pink")
    plt.plot(x_train, t_train, "bo")
    plt.legend(["sin", "model"])
    plt.xlim(X_MIN, X_MAX)
    plt.ylim(T_MIN, T_MAX)
    plt.xlabel("x")
    plt.ylabel("t")
    plt.title("N = %d, M = %d" % (N, M))
    plt.show()

if __name__ == "__main__":
    main()

