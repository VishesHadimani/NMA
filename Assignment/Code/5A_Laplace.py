import numpy as np
import matplotlib.pyplot as plt

def laplace_2d(grid_size, max_iter=1000):
    phi = np.zeros(grid_size)
  
    phi[0, :] = 100  
    phi[-1, :] = 100  
    phi[:, 0] = 0  
    phi[:, -1] = 0  
    
    for _ in range(max_iter):
        phi_new = np.copy(phi)
        
        for i in range(1, grid_size[0] - 1):
            for j in range(1, grid_size[1] - 1):
                phi_new[i, j] = 0.5 * (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1])
        
        phi = np.copy(phi_new)

    print("\nFinal Values of φ (Laplace's Equation) with 4 Decimal Places:")
    np.set_printoptions(precision=4)  
    print(phi)  
    return phi


grid_size = (10,10) 
phi = laplace_2d(grid_size)

plt.imshow(phi, cmap='hot', origin='lower')
plt.colorbar(label='Potential (φ)')
plt.title("Solution to Laplace's Equation")
plt.show()
