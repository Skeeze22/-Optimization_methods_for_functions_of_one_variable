import math

# method of dividing a segment in half
def DichotomyMethod(f, a_start, b_start, eps):
    a = a_start
    b = b_start
    delta = eps / 2
    interval_length = b - a
    iters = 0
    function_calcs = 0
    while interval_length > eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
        interval_length = b - a
        function_calcs += 2
        iters += 1
    return (a + b) / 2.0, function_calcs, iters

# the golden ratio method
def GoldenSectionMethod(f, a_start, b_start, eps):
    a = a_start
    b = b_start
    interval_length = b - a
    x1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
    x2 = a + (math.sqrt(5) - 1) / 2 * (b - a)
    y1 = f(x1)
    y2 = f(x2)
    iters = 0
    function_calcs = 2
    while interval_length > eps:
        if y1 > y2:
            a = x1
            x1 = x2
            x2 = a + (math.sqrt(5) - 1) / 2 * (b - a)
            y1 = y2
            y2 = f(x2)
            function_calcs += 1
        else:
            b = x2
            x2 = x1
            x1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
            y2 = y1
            y1 = f(x1)
            function_calcs += 1
        interval_length = b - a
        iters += 1
    return (a + b) / 2.0, function_calcs, iters

# Fibonacci method
def FibonacciMethod(f, a_start, b_start, eps):
    a = a_start
    b = b_start
    iters = 0
    function_calcs = 0
    n = 0
    while f(n) < (b - a) / eps:
        function_calcs += 1
        n += 1
    x1 = a + (f(n - 2) / f(n)) * (b - a)
    function_calcs += 2
    y1 = f(x1)
    function_calcs += 1
    x2 = a + (f(n - 1) / f(n)) * (b - a)
    function_calcs += 2
    y2 = f(x2)
    function_calcs += 1
    for k in range(0, n - 2):
        if y1 <= y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = a + (f(n - k - 3) / f(n - k - 1)) * (b - a)
            function_calcs += 2
            y1 = f(x1)
            function_calcs += 1
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + (f(n - k - 2) / f(n - k - 1)) * (b - a)
            function_calcs += 2
            y2 = f(x2)
            function_calcs += 1
    x2 = x1 + eps
    y2 = f(x2)
    function_calcs += 1
    iters = n - 2
    if y1 <= y2:
        b = x1
    else:
        a = x1
    return (a + b) / 2.0, function_calcs, iters