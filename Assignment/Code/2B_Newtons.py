# Newton’s Forward and Backward Difference Formulae (Equal Intervals)

import numpy as np

def newton_forward(x_points, y_points, x):
    n = len(x_points)
    h = x_points[1] - x_points[0]
    u = (x - x_points[0]) / h

    # Build the forward difference table
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_points

    for col in range(1, n):
        for row in range(n - col):
            diff_table[row, col] = diff_table[row + 1, col - 1] - diff_table[row, col - 1]

    result = diff_table[0, 0]
    u_term = 1
    for i in range(1, n):
        u_term *= (u - (i - 1))
        result += (u_term * diff_table[0, i]) / np.math.factorial(i)

    return result

def newton_backward(x_points, y_points, x):
    n = len(x_points)
    h = x_points[1] - x_points[0] 
    u = (x - x_points[-1]) / h

    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_points

    for col in range(1, n):
        for row in range(n - 1, col - 2, -1):
            diff_table[row, col] = diff_table[row, col - 1] - diff_table[row - 1, col - 1]

    result = diff_table[-1, 0]
    u_term = 1
    for i in range(1, n):
        u_term *= (u + (i - 1))
        result += (u_term * diff_table[-1, i]) / np.math.factorial(i)

    return result

x_points = [100,150,200,250,300,350,400]
y_points = [10.63,13.03,15.04,16.81,18.42,19.90,21.27]
x_to_fwd_interpolate = 160
x_to_bwd_interpolate = 410

print("Forward Interpolation value at x =", x_to_fwd_interpolate, "is", newton_forward(x_points, y_points, x_to_fwd_interpolate))
print("Backward Interpolation value at x =", x_to_bwd_interpolate, "is", newton_backward(x_points, y_points, x_to_bwd_interpolate))
