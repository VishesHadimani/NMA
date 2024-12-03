#Lagrange's Interpolation (Unequal Intervals)

def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    result = 0

    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term

    return result

x_points = [5,7,11,13,17]
y_points = [150,392,1452,2366,5202]
x_to_interpolate = 9

print("Interpolated value at x =", x_to_interpolate, "is", lagrange_interpolation(x_points, y_points, x_to_interpolate))
