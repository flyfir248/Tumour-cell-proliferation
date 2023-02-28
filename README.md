# Tumour-cell-proliferation
A tumour cell proliferation study


### README file for Tumor-Immune System Dynamics Model
This is a Python implementation of a mathematical model that describes the dynamics of a tumor and the immune system. The model is described by a system of ordinary differential equations (ODEs), which are solved using the odeint function from the scipy.integrate library.

### Model Parameters
The model includes the following parameters:

n: Hill coefficient for the immune response

k1: production rate of IL-2 by T-helper cells

K: carrying capacity of environment

alpha: immune-mediated killing rate of tumor cells

beta: recruitment rate of immune cells to tumor site

delta: death rate of immune cells

eta: rate of transition from Trr cells to Th cells

xi: rate of proliferation of Th cells

nu: death rate of Tc cells

mu: death rate of Th cells

k3: Hill coefficient for the Trr cells' effect on Th cells

zeta: rate of killing of Tc cells by Trr cells

epsilon: rate of apoptosis of Tn cells

r: intrinsic growth rate of tumor


### Running the Model
To run the model, make sure to have the required libraries (numpy, scipy, and matplotlib) installed. Then, simply run the Python script. The initial conditions and time points are defined in the script, but can be changed as desired.

The output of the script is a plot that shows the dynamics of the tumor and the different immune cell types over time.

### Additional Notes
This model is a simplified representation of the complex interactions between a tumor and the immune system. It assumes certain simplifying assumptions and neglects some important factors. Therefore, the results should be interpreted with caution and should not be used for clinical decision-making.

This implementation of the model has been fixed to correct a few syntax errors that were present in the original code.
