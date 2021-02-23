from interval_with_minimum import GetIntervalWithMinimum
from zadanie_a import DichotomyMethod, GoldenSectionMethod
from zadanie_b import PauellaMethod
from zadanie_c import newton, sred

# Original assignment
# f(x)=2*(x^2)+(16/x) xE[1;5]

# Original function
def F(x):
    return (2*pow(x, 2))+(16/x)
# first derivative
def Fsht(x):
    return (4*x)-(16/(pow(x, 2)))
# second derivative
def Fsht2(x):
    return 4+(32/(pow(x,3)))

def main():
    print("Getting an interval with minimum function")
    print(GetIntervalWithMinimum(F, 1, 0.0001))
    print("A) golden ratio")
    print(GoldenSectionMethod(F, 1, 5, 0.0001))
    print("A) Dividing a segment in half")
    print(DichotomyMethod(F, 1, 5, 0.0001))
    print("B) Powell's method")
    print(PauellaMethod(F, 0.01, 1, 0.0001))
    print("C) Newton-Raphson method")
    print(newton(F, Fsht, Fsht2, 1, 0.0001))
    print("C) midpoint method")
    print(sred(F, Fsht, 1, 5, 0.0001))

main()
