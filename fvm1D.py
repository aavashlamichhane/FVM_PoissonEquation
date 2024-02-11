import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# Define the problem parameters
L = 1.0  # Length of the domain
Nx = 50  # Number of cells
dx = L / Nx  # Cell center spacing
left_boundary = 0.0
right_boundary = 0.0
def source_term(x): #Can be modified for specific problem
    return 1  

# Step 1: Discretize the domain
x_values = np.linspace(0, L, Nx+1)
cell_centers = 0.5 * (x_values[1:] + x_values[:-1])

# Step 2: Initialize matrices for the linear system
# Using a tri-diagonal matrix to represent the Laplacian
A = diags([-1, 2, -1], [-1, 0, 1], shape=(Nx, Nx),format='csr') / dx**2
b = np.zeros(Nx)

# Step 3: Evaluating Source term function
for i in range(1, Nx-1):
    b[i] = -source_term(cell_centers[i])

# Step 4: Apply boundary conditions
# In this example, using Dirichlet boundary conditions (u=0 at both ends)
# Modify based on your specific boundary conditions
b[0] = left_boundary
b[-1] = right_boundary

# Step 5: Solve the linear system
u = spsolve(A, b)

# print(type(u))
# print(u)

# Step 6: Plot the results
plt.plot(cell_centers, u, marker='o', label='Solution')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Solution of Poisson Equation')
plt.legend()
plt.show()