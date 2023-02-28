import numpy as np
from scipy.integrate import odeint

# Define the parameters of the model
n = 3
k1 = 0.9  # constant for Tnaive
K = 1.0  # carrying capacity of environment
alpha = 0.01  # immune-mediated killing rate of tumor cells
beta = 0.05  # recruitment rate of immune cells to tumor site
delta = 0.1  # death rate of immune cells
k1 = 0.1  # production rate of IL-2 by T-helper cells
eta = 0.5
xi = 0.6
nu = 0.5
mu = 0.4
k3 = 0.4
zeta = 0.6
epsilon = 0.4
r = 0.1  # intrinsic growth rate of tumor

# Define the system of differential equations
def model(y, t):
    C, Tn, Trr, Tc, Th = y
    dCdt = beta*Th - alpha*((C**n)/((C**n)+(K**n)))*Tc - beta*C
    dTndt = k1 - alpha*((C**n)/((C**n)+(K**n)))*Tn - epsilon*Tn
    dTrrdt = delta*(1-(Trr/k3))*Trr - zeta*Tc - eta*Trr
    dTcdt = alpha*((C**n)/((C**n)+(K**n)))*Tn - nu*Tc
    dThdt = xi*(beta+(Trr**n)/((Trr**n)+(k3**n)))-mu*Th
    return [dCdt, dTndt, dTrrdt, dTcdt, dThdt]

# Define the initial conditions and time points
y0 = [0.1, 0.1, 0.1, 0.1, 0.1]
t = np.linspace(0, 100, 101)

# Solve the system of differential equations
sol = odeint(model, y0, t)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], label='C')
plt.plot(t, sol[:, 1], label='Tn')
plt.plot(t, sol[:, 2], label='Trr')
plt.plot(t, sol[:, 3], label='Tc')
plt.plot(t, sol[:, 4], label='Th')
plt.xlabel('Time')
plt.ylabel('Density/Concentration')
plt.legend()
plt.show()