import math

def f(t, y):
    return -20*y + 7*math.e**(-1.5*t)

def euler_advance(h, t0, y0, tf):
    n = int((tf - t0) / h)
    t = [t0]
    y = [y0]
    
    for i in range(n): 
        y.append(round(y[i] + h/2 * (f(t[i], y[i]) + f(t[i] + h, y[i] + h * f(t[i], y[i]))), 5))
        t.append(t[i] + h)

    return t, y

h = 0.01
# h = 0.0001
t0 = 0
y0 = 5
tf = 0.04

t, y = euler_advance(h, t0, y0, tf)

for i in range(len(t)):
    print("t =", t[i], ", y =", y[i])