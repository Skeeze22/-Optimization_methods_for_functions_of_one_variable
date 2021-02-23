# Newton-Raphson method
def newton(f, f1sht, f2sht, x0, eps, number_of_max_iterations=100):
    x1 = 0
    if abs(x0-x1) <= eps and abs((x0-x1)/x0) <= eps:
        return f(x0), x0, 0
    k = 1
    while k <= number_of_max_iterations:
        x1 = x0 - (f1sht(x0)/f2sht(x0))
        if abs(x0-x1) <= eps and abs((x0-x1)/x0) <= eps:
            return f(x1), x1, k
        x0 = x1
        k += 1
        # Stop the method if the maximum number of iterations is reached
        if k > number_of_max_iterations:
            print("Error exited, too many iterations")
    return f(x1), x1, k

# Midpoint method
def sred(F, Fsht, a, b , eps):
    x = (a+b)/2
    k = 0
    pz = Fsht(x)
    while abs(pz) > eps:
        if pz < 0:
            a = x
        else:
            b = x
        x = (a+b)/2
        pz = Fsht(x)
        k += 1
    return F(x), x, k

