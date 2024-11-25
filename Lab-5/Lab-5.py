import numpy as np


def f(x):
    return 2 * x**8 + 3 * x**7 + 5 * x**5 - 2

a, b = 1, 5


def build_quadrature_formula(nodes):
    
    n = len(nodes)
    weights = []
    for i in range(n):
       
        li = lambda x: np.prod([(x - nodes[j]) / (nodes[i] - nodes[j]) for j in range(n) if j != i])
       
        integral_li = np.trapz([li(x) for x in np.linspace(a, b, 1000)], np.linspace(a, b, 1000))
        weights.append(integral_li)
   
    integral = sum(weights[i] * f(nodes[i]) for i in range(n))
    return integral, weights

nodes = np.array([1, 2, 3, 4, 5])
I_quad, weights = build_quadrature_formula(nodes)

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    midpoints = [a + h * (i + 0.5) for i in range(n)]
    return h * sum(f(x) for x in midpoints)

I_mid = midpoint_rule(f, a, b, n=4)

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Кількість розбиттів (n) має бути парною.")
    h = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    return (h / 3) * (
        f(x_vals[0])
        + 4 * sum(f(x_vals[i]) for i in range(1, n, 2))
        + 2 * sum(f(x_vals[i]) for i in range(2, n, 2))
        + f(x_vals[-1])
    )

I_simpson = simpson_rule(f, a, b, n=4)

print("1. Квадратурна формула інтерполяційного типу:")
print("   Значення інтегралу:", I_quad)
print("   Вагові коефіцієнти:", weights)

print("\n2. Формула середніх прямокутників:")
print("   Значення інтегралу:", I_mid)

print("\n3. Формула Сімпсона:")
print("   Значення інтегралу:", I_simpson)
