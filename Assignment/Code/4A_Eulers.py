# Euler’s Method
import numpy as np
def euler_method_verbose(f, x0, y0, x_end, h):
    x = x0
    y = y0
    steps = int((x_end - x0) / h)
    
    print(f"x = {x}, y = {y}")
    for step in range(steps):
        y += h * f(x, y)  
        x += h
        print(f"Step {step + 1}: x = {x}, y = {y}")
    
    print("\nFinal result:")
    print(f"y({x_end}) = {y}")
    return y


f = lambda x, y: x + y  
x0 = 0  
y0 = 1  
x_end = 1 
h = 0.1 

result = euler_method_verbose(f, x0, y0, x_end, h)
