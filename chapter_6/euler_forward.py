import math

def f(t, y):
    # return -20*y + 7*math.e**(-1.5*t)
    return y + t*t*y + 1

def euler_forward(h, t0, y0, tf):
    n = int((tf - t0) / h)
    t = [t0]
    y = [y0]
    
    for i in range(n):
        # t[i] = round(t[i], 2)
        t.append(t[i] + h)

    for i in range(n): 
        # rounding result 5 number after comma
        y.append(round(y[i] + h * f(t[i], y[i]), 5))
    
    return t, y

h = 0.1
# h = 0.0001
t0 = 0
y0 = 1
tf = 0.2

t, y = euler_forward(h, t0, y0, tf)

for i in range(len(t)):
    print("t =", t[i], ", y =", y[i])