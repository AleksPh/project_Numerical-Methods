import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**3 + x**2 - 4*x - 4

def f1_prime(x):
    return 3*x**2 + 2*x - 4

def f2(x):
    return x**3 - 4*x**2 - 4*x + 16

def g(x):
    return (4*x**2 + 4*x - 16) / x  


def newton_method(x0, epsilon=1e-6, max_iter=100):
    iterations = []
    x = x0
    for i in range(max_iter):
        x_new = x - f1(x) / f1_prime(x)
        if abs(x_new - x) < epsilon:
            break
        x = x_new
        iterations.append([i + 1, round(x, 6), round(f1(x), 6)])
    return iterations

def simple_iteration_method(x0, epsilon=1e-6, max_iter=100):
    iterations = []
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < epsilon:
            break
        x = x_new
        iterations.append([i + 1, round(x, 6), round(f2(x), 6)])
    return iterations

def plot_graph_f1():
    x = np.linspace(-5, 5, 400)
    y = f1(x)
    plt.plot(x, y, label=r'$f(x) = x^3 + x^2 - 4x - 4$')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title("Graph of $f(x) = x^3 + x^2 - 4x - 4$")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_graph_f2():
    x = np.linspace(-5, 5, 400)
    y = f2(x)
    plt.plot(x, y, label=r'$f(x) = x^3 - 4x^2 - 4x + 16$')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title("Graph of $f(x) = x^3 - 4x^2 - 4x + 16$")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def print_table(method, results):
    print(f"Results for {method} Method:")
    print(f"{'Iteration':<12}{'x':<15}{'f(x)'}")
    print("-" * 40)
    for result in results:
        print(f"{result[0]:<12}{result[1]:<15}{result[2]}")
    print("-" * 40)

def main():
    print("Method 1: Newton's Method")
    x0_newton = float(input("Enter initial guess for Newton's method: "))
    results_newton = newton_method(x0_newton)
    print_table("Newton", results_newton)

    print("\nMethod 2: Simple Iteration Method")
    x0_iteration = float(input("Enter initial guess for Iteration method: "))
    results_iteration = simple_iteration_method(x0_iteration)
    print_table("Simple Iteration", results_iteration)

    plot_graph_f1()
    plot_graph_f2()

if __name__ == "__main__":
    main()
