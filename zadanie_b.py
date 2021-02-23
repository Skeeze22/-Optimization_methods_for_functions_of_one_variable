# choosing x1 and x2 for optimal _x
def opt(w, a, b, c, h):
    if w < a:
        c = b
        while a > w:
            a -= h
    elif w > c:
        a = b
        while c < w:
            c += h
    elif w < b:
        c = b
    elif w > b:
        a = b
    else:
        w = b
    return a, w, c

# Powell's method
def PauellaMethod(f, h, x1, eps):
    k = 0
    x2 = x1 + h
    f1 = f(x1)
    f2 = f(x2)
    if f1 > f2:
        x3 = x1 + 2 * h
        _x = x2
    else:
        x3 = x1 - h
        _x = x1
    f3 = f(x3)
    # preliminarily the minimum of the function in the minimum of three values, and the required minimum in the maximum
    fmin = min(f1, f2, f3)
    f_x = max(f1, f2, f3)
    # sorting three points - arranging in order
    x1, x2, x3 = sorted([x1, x2, x3])
    i = 1
    # iteration loop
    while abs((fmin - f_x) / f_x) > eps:
        # definition of boundary points x1 and x2, for _x - "best" argument, must be x1 <_x <x2
        x1, x2, x3 = opt(_x, x1, x2, x3, h)
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
        # finding the minimum of three functions
        tmp = sorted([(f1, x1), (f2, x2), (f3, x3)])
        fmin, xmin = tmp[0]
        # definition of the coefficient for quadratic approximation
        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * (((f3 - f1) / (x3 - x1)) - ((f2 - f1) / (x2 - x1)))
        # definition of _x and f values (_x)
        _x = (x2 + x1) / 2 - a1 / (2 * a2)
        f_x = f(_x)
        i +=1
    return f1, f2, f3, fmin, _x, i
