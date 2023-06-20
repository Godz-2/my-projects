import statistics

import sympy
import math
from sympy import *
from sympy.solvers import solve
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
from colorama import *
from statistics import *


# Functions For Linear Equations Solving
def linear_equation_solving(number_variables):
    variable = symbols('x y z w')
    equations = []
    for i in range(number_variables):
        equation = input("Enter The Equation\n0 = ")
        eq = Eq(sympify(equation), 0)
        equations.append(eq)
    print("\n")
    text = Fore.RED + "Calculating..." + Style.BRIGHT
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
    text = Fore.GREEN + "Calculating..." + Style.BRIGHT
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
    text = Fore.CYAN + "Calculating..." + Style.BRIGHT
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
    text = Fore.LIGHTBLUE_EX + "Calculating..." + Style.BRIGHT
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
    n = int(input("order of derivative: "))
    df = sympy.diff(f_1, x, n)
    print("\n")
    text = Fore.MAGENTA + "Calculating..." + Style.BRIGHT
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(2.0)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()
    print("\n")
    print("The Derivative is = ", df)
    print("\n")


def derivative_at_point():
    x = symbols('x')
    f = input("Enter Your Function: ")
    f_1 = sympify(f)
    n = int(input("order of derivative: "))
    df = sympy.diff(f_1, x, n)
    print("The Derivative is = ", df)
    c = float(input("Enter The Point, x = "))
    point = df.subs(x, c)
    print("\n")
    text = Fore.CYAN + "Calculating..." + Style.BRIGHT
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
    text = Fore.BLUE + "Calculating..." + Style.BRIGHT
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
    print(Fore.RED + "# NOTE For infinite Limit use oo or -oo" + Style.BRIGHT)
    c = float(input(Fore.GREEN + "Enter the Lower limit: " + Style.BRIGHT))
    c1 = float(input(Fore.GREEN + "Enter the upper limit: " + Style.BRIGHT))
    print("\n")
    text = Fore.BLUE + "Calculating..." + Style.RESET_ALL
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
    text = Fore.GREEN + "Calculating..." + Style.BRIGHT
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
    text = Fore.LIGHTBLUE_EX + "Calculating..." + Style.BRIGHT
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
    text = Fore.GREEN + "Calculating..." + Style.BRIGHT
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
    plt.title('Graph-Plot')
    f = input(Fore.LIGHTRED_EX + "Enter The Function To Plot in Graph, f(x) = y =  " + Style.RESET_ALL)
    y = sympify(f)

    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10

    points = 100 * (xmax - xmin)
    x = np.linspace(xmin, xmax, points)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], 'b')
    plt.plot([0, 0], [ymin, ymax], 'b')
    y_values = [y.subs('x', xi) for xi in x]
    plt.plot(x, y_values, label=y, color='orange')
    plt.legend()
    plt.grid(True)
    plt.show()


print(Fore.RED + "INSTRUCTIONS\n" + Style.BRIGHT)
print(Fore.RED + "Write Multiplication in * Form And Power In ** Form\n" + Style.RESET_ALL)
print("\n")
print(Fore.LIGHTBLUE_EX + "----------------------------------------------------------------------" + Style.BRIGHT)
if __name__ == '__main__':
    while True:
        print(
            Fore.BLUE + "Press 1 For Linear Equation Solving (Upto 4 Variables)\nPress 2 For Roots Of Polynomial (Upto Bi-Quadritic)\nPress 3 For Calculus\nPress 4 For Graph Plotting\nPress 5 For Misc\nPress 6 For Central Tendency)\n0 for quit" + Style.RESET_ALL)
        print()
        user = int(input(Fore.LIGHTGREEN_EX + "Which Type Of Operation Do You Want To Do\n" + Style.BRIGHT))
        print(
            Fore.LIGHTGREEN_EX + "------------------------------------------------#----------------------------------------------" + Style.RESET_ALL)
        print("\n")

        if user == 1:
            number = int(input(Fore.LIGHTYELLOW_EX + "Enter The No of Variables: " + Style.BRIGHT))
            linear_equation_solving(number)
            print("\n")
        elif user == 2:
            user_1 = int(input(
                Fore.LIGHTYELLOW_EX + "Press 1 For Roots of Quadritic\nPress 2 For Roots of Cubic\nPress 3 for Roots Bi-Quadritic\n" + Style.BRIGHT))
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
                Fore.CYAN + "Press 1 For Differentiation\nPress 2 For Derivative Value at a Given Point\nPress 3 For Indefinite Integration\nPress 4 For Definite Integration\nPress 5 For Limit Evaluation\n" + Style.BRIGHT))
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
            user_1 = int(input(
                Fore.GREEN + "Enter The Operation\n1 For Factorial Calculation\n2 For nth Root Calculation\n" + Style.BRIGHT))
            print("\n")
            if user_1 == 1:
                factorial()
            elif user_1 == 2:
                nth_root()
            else:
                print("Invalid Input! Try Again\n")
        elif user == 6:
            user_1 = int(input(Fore.BLUE + "Press 1 For Mean\nPress 2 For Median\nPress 3 For Mode\n" + Style.BRIGHT))
            print("\n")
            try:
                if user_1 == 1:
                    l = []
                    obs = int(input("Enter The Number Of Observation: "))
                    print(Fore.LIGHTYELLOW_EX + "Enter The Observations\n" + Style.RESET_ALL)
                    for i in range(obs):
                        a = int(input())
                        l.append(float(a))

                    print("\n")
                    print(Fore.GREEN + "The Mean is = " + Style.BRIGHT, statistics.mean(l))
                    print("\n")
                elif user_1 == 2:
                    m = []
                    obs = int(input("Enter The Number Of Observation: "))
                    print(Fore.LIGHTYELLOW_EX + "Enter The Observations\n" + Style.RESET_ALL)
                    for i in range(obs):
                        a = int(input())
                        m.append(float(a))

                    print("\n")
                    print(Fore.LIGHTRED_EX + "The Median Is = " + Style.BRIGHT, statistics.median(l))
                    print("\n")
                elif user_1 == 3:
                    n = []
                    obs = int(input("Enter The Number Of Observation: "))
                    print(Fore.LIGHTYELLOW_EX + "Enter The Observations\n" + Style.RESET_ALL)
                    for i in range(obs):
                        a = int(input())
                        n.append(int(a))

                    print("\n")
                    print(Fore.CYAN + "The Mode Is = " + Style.BRIGHT, statistics.mode(l))
                    print("\n")
            except:
                print("Invalid Input!\n")

        elif user == 0:
            break

    print((Fore.LIGHTBLUE_EX + "THANK YOU FOR USING!\n" + Style.BRIGHT))
