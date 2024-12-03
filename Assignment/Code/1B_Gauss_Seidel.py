import numpy as np

def gauss_seidel_verbose(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros_like(b, dtype=float)

    print("Iteration results:")
    for iteration in range(max_iterations):
        x_old = np.copy(x)
        
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_) / A[i][i]

        print(f"Iteration {iteration + 1}: {x}")
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            print("\nConverged!\n")
            print("Final Solution:", x)
            return x

    print("\nDid not converge within the maximum number of iterations.\n")
    print("Last Solution:", x)
    return x

A = np.array([[5, -2, 3],
              [3, 9, 1],
              [2, -1, -7]], dtype=float)
b = np.array([-1, 2, 3], dtype=float)

gauss_seidel_verbose(A, b)
