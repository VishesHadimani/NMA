# Fourth Order Runge-Kutta Method
import numpy as np
def runge_kutta_4th_order_verbose(f, x0, y0, x_end, h):
    x = x0
    y = y0
    steps = int((x_end - x0) / h)
    
    print(f"x = {x}, y = {y}")
    for step in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        print(f"Step {step + 1}: k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}")
        
        y += (k1 + 2*k2 + 2*k3 + k4) / 6  
        x += h
        print(f"After Step {step + 1}: x = {x}, y = {y}")
    
    print("\nFinal result:")
    print(f"y({x_end}) = {y}")
    return y

f = lambda x, y: (y**2 - x**2)/(y**2 + x**2) 
x0 = 0  
y0 = 1 
x_end = 1 
h = 0.1  

result = runge_kutta_4th_order_verbose(f, x0, y0, x_end, h)
