# получить n-ое число из последовательности Фиббоначчи
def GetFibonacciNumber(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n):
            a, b = b, a + b
        return b

    # получить n чисел из последовательности Фиббоначчи


def GetFibonacciSequence(n):
    sequence = []
    a = 0
    b = 1
    if n == 0:
        return sequence.append(a)
    elif n == 1:
        return sequence.extend([a, b])
    elif n == 2:
        return sequence.extend([a, b, a + b])
    else:
        sequence.extend([a, b, a + b])
        m = 4
        while m < n + 1:
            for _ in range(2, m):
                a, b = b, a + b
            sequence.append(b)
            a = 0
            b = 1
            m += 1
        return sequence