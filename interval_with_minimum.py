# поиск интервала, содержащего минимум с заданной точностью eps
def GetIntervalWithMinimum(f, x0, eps):
    delta = eps / 2
    x1 = 0
    h = 0
    f0 = f(x0)
    if f0 > f(x0 + delta):
        x1 = x0 + delta
        h = delta
    elif f(x0) > f(x0 - delta):
        x1 = x0 - delta
        h = - delta
    h = 2 * h
    f1 = f(x1)
    x2 = x1 + h
    f2 = f(x2)
    i = 1
    while f1 > f2:
        x0 = x1
        f0 = f1
        x1 = x2
        f1 = f2
        h = 2 * h
        x2 = x1 + h
        f2 = f(x2)
        i += 1
    if h > 0:
        return x0, x2
    else:
        return x2, x0