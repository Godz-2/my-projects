import sympy
import math
from sympy import *
from sympy.solvers import solve
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
import time
import sys


# Functions For Linear Equations Solving
def linear_equation_solving(number_variables):
    variable = symbols('x y z w')
    equations = []
    for i in range(number_variables):
        equation = input("Enter The Equation\n0 = ")
        eq = Eq(sympify(equation), 0)
        equations.append(eq)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("Solutions Are Given Below\n")
    sol = solve(equations, variable)
    print(sol)


# ----------------------------------------------------------------------------------------------------------------------
# Polynomial Functions

def quadritic():
    x = symbols('x')
    eq = input("Enter The Quadritic Equation\n0=")
    eq_1 = Eq(sympify(eq), 0)
    sol = solve(eq_1)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("Roots are given below\n")
    for s in sol:
        print("x =", s, ",", end=" ")


def cubic():
    x = symbols('x')
    eq = input("Enter the Cubic Equation\n0=")
    print("\n")
    eq_1 = Eq(sympify(eq), 0)
    sol = solve(eq_1)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("Roots Are Given below\n")
    for s in sol:
        print("x =", s, ",", end=" ")


def bi_quad():
    x = symbols('x')
    eq = input("Enter the Equation\n0=")
    eq_1 = Eq(sympify(eq), 0)
    sol = solve(eq_1)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("Root are Given below\n")
    time.sleep(3.0)
    for s in sol:
        print("x = ", s, ",", end=" ")


# ----------------------------------------------------------------------------------------------------------------------
# Calculus

def derivative():
    x = symbols('x')
    f = input("Enter Your Function: ")
    f_1 = sympify(f)
    df = sympy.diff(f_1, x)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    print("The Derivative is = ", df)


def derivative_at_point():
    x = symbols('x')
    f = input("Enter Your Function: ")
    f_1 = sympify(f)
    df = sympy.diff(f_1, x)
    print("The Derivative is = ", df)
    c = float(input("Enter The Point, x = "))
    point = df.subs(x, c)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    print("The Derivative at x = ", c, "is = ", point)


def indefinite_integrate():
    x = symbols('x')
    f = input("Enter The Function: ")
    f_1 = sympify(f)
    inT = sympy.integrate(f_1, x)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    print("The Value Integral = ", inT, "+C")


def definite_integration():
    x = symbols('x')
    f = input("Enter the Function: ")
    f_1 = sympify(f)
    print("# NOTE For infinite Limit use oo or -oo")
    c = float(input("Enter the Lower limit: "))
    c1 = float(input("Enter the upper limit: "))
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    inT = sympy.integrate(f_1, (x, c, c1))
    print("The Value Of Given Integral is = ", inT)


def lim():
    variables = symbols('x')
    f = input("Enter The Function: ")
    sympify(f)
    b = float(input("Enter The Evaluation Point or Limiting Point: "))
    lim_result = limit(f, variables, b)
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    print("Result Is = ", lim_result)


# Some Miscellaneous Operations
# ----------------------------------------------------------------------------------------------------------------------

def factorial():
    num = int(input("Enter The Number: "))
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    print("The Factorial Of", num, "is = ", math.factorial(num))


def nth_root():
    n = float(input("Enter The Number: "))
    p = float(input("Enter nth Root: "))
    print("\n")
    text = "Calculating..."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    print(n, "^", p, "=", pow(n, p))


# Graph-Plotting
# ----------------------------------------------------------------------------------------------------------------------

def plot():
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Graph')
    plt.grid(True)
    f = input("Enter The Function To Plot, f(x) =  ")
    f1 = sympify(f)
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.01)
    y = [f1.subs('x', val) for val in x]
    plt.plot(x, y, label=f1, color='orange')
    plt.legend()
    plt.show()

print("Write Multiplication in * Form And\nPower In ** Form\n")
print("\n")
print("----------------------------------------------------------------------")
if __name__ == '__main__':
    while True:
        print(
            "Press 1 For Linear Equation Solving (Upto 4 Variables)\nPress 2 For Roots Of Polynomial (Upto Bi-Quadritic)\nPress 3 For Calculus\nPress 4 For Graph Plotting\nPress 5 For Misc\n0 for quit")
        print()
        user = int(input("Which Type Of Operation Do You Want To Do\n"))
        print("------------------------------------------------#----------------------------------------------")
        print("\n")

        if user == 1:
            number = int(input("Enter The No of Variables: "))
            linear_equation_solving(number)
            print("\n")
        elif user == 2:
            user_1 = int(input("Press 1 For Quadritic\nPress 2 For Cubic\nPress 3 Bi-Quadritic\n"))
            if user_1 == 1:
                quadritic()
            elif user_1 == 2:
                cubic()
                print("\n")
            elif user_1 == 3:
                bi_quad()
            else:
                print("Invalid Input! Try Again\n")
            print("\n")
        elif user == 3:
            user_1 = int(input(
                "Press 1 For Differentiation\nPress 2 For Derivative Value at a Given Point\nPress 3 For Indefinite Integration\nPress 4 For Definite Integration\nPress 5 For Limit Evaluation\n"))
            if user_1 == 1:
                derivative()
            elif user_1 == 2:
                derivative_at_point()
            elif user_1 == 3:
                indefinite_integrate()
            elif user_1 == 4:
                definite_integration()
            elif user_1 == 5:
                lim()
            else:
                print("Invalid Input! Try Again\n")
                print("\n")
        elif user == 4:
            plot()
        elif user == 5:
            user_1 = int(input("Enter The Operation\n1 For Factorial Calculation\n2 For nth Root Calculation\n"))
            print("\n")
            if user_1 == 1:
                factorial()
            elif user_1 == 2:
                nth_root()
            else:
                print("Invalid Input! Try Again\n")
        elif user == 0:
            break

    print("Thank You!\n")
