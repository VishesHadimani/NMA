# Numerical Integration using Simpson’s 1/3 Rule(Single)
import numpy as np
def simpsons_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")
    
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    integral = y[0] + y[-1]  
    integral += 4 * sum(y[i] for i in range(1, n, 2))  
    integral += 2 * sum(y[i] for i in range(2, n, 2)) 

    integral *= h / 3
    return integral

# Example Usage:
f = lambda x: 2*x - x**2  
a, b = 0, 3         
n = 6       

print("Integral using Simpson's 1/3 rule:", simpsons_one_third(f, a, b, n))
