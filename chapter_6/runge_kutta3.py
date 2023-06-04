# Example: Solve the differential equation dy/dx = x + y with y(0) = 1
def f(x, y):
    return x + y

def runge_kutta3_simpson13(f, x0, y0, h, n):
    """
    f: Function representing the differential equation dy/dx = f(x, y)
    x0: Initial value of x
    y0: Initial value of y at x = x0
    h: Step size
    n: Number of steps
    """
    x = [x0]
    y = [y0]

    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h, y[i] - k1 + 2*k2)
        x.append(x[i] + h)
        y.append(y[i] + (k1 + 4*k2 + k3) / 6)

    return x, y

x0 = 0
y0 = 1
h = 0.1
n = 10

x, y = runge_kutta3_simpson13(f, x0, y0, h, n)

# Print the results
for i in range(len(x)):
    print(f"x = {x[i]}, y = {y[i]}")