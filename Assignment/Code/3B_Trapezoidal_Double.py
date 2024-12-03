# Evaluation of Double Integrals by Trapezoidal Rule

def trapezoidal_double_integral(f, a, b, c, d, m, n):
    h_x = (b - a) / m
    h_y = (d - c) / n

    x = [a + i * h_x for i in range(m + 1)]
    y = [c + j * h_y for j in range(n + 1)]

    integral = 0
    for i in range(m + 1):
        for j in range(n + 1):
            weight = 1
            if i == 0 or i == m:
                weight /= 2
            if j == 0 or j == n:
                weight /= 2
            integral += weight * f(x[i], y[j])

    integral *= h_x * h_y
    return integral

f = lambda x, y: 1/(x * y)
a, b = 1, 1.4            
c, d = 2, 2.4          
m, n = 4, 4 

print("Double integral using Trapezoidal rule:", trapezoidal_double_integral(f, a, b, c, d, m, n))
