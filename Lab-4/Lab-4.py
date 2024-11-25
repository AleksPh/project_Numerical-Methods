import numpy as np

def power_method_inverse(A, tol=1e-9, max_iter=100):
    n = A.shape[0]
    x = np.random.rand(n)  
    x = x / np.linalg.norm(x)
    
    for i in range(max_iter):
        y = np.linalg.solve(A, x)  
        y_norm = np.linalg.norm(y)
        x_new = y / y_norm
        if np.linalg.norm(x_new - x) < tol:
            eigenvalue = 1 / y_norm
            return eigenvalue, x_new
        x = x_new

    raise ValueError("Степеневий метод не збігся за задану кількість ітерацій.")

def jacobi_method(A, tol=1e-9, max_iter=100):
    n = A.shape[0]
    V = np.eye(n)
    for _ in range(max_iter):
        max_val = 0
        p, q = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j

        if max_val < tol:
            return np.diag(A), V
        
        theta = 0.5 * np.arctan2(2 * A[p, q], A[p, p] - A[q, q])
        R = np.eye(n)
        R[p, p] = R[q, q] = np.cos(theta)
        R[p, q] = -np.sin(theta)
        R[q, p] = np.sin(theta)
        
        A = R.T @ A @ R
        V = V @ R

    raise ValueError("Метод Якобі не збігся за задану кількість ітерацій.")

def newton_method(f, jacobian, x0, tol=1e-6, max_iter=10):
    x = np.array(x0, dtype=float)
    for _ in range(max_iter):
        J = jacobian(x)
        F = f(x)
        delta_x = np.linalg.solve(J, -F)
        x_new = x + delta_x
        if np.linalg.norm(delta_x) < tol:
            return x_new
        x = x_new

    raise ValueError("Метод Ньютона не збігся за задану кількість ітерацій.")

A = np.array([
    [5, 0, 2, 1],
    [0, 4, 0, 1],
    [2, 0, 2, 0],
    [1, 1, 0, 3]
], dtype=float)


inverse_eigenvalue, eigenvector = power_method_inverse(A)
print("Найменше власне значення (степеневий метод):", inverse_eigenvalue)


eigenvalues, _ = jacobi_method(A)
print("Власні значення (метод Якобі):", eigenvalues)

def system_equations(x):
    return np.array([
        5 * x[0] - 6 * x[1] + 20 * np.log10(x[0]) + 16,
        2 * x[0] + x[1] - 10 * np.log10(x[1]) - 4
    ])

def jacobian_matrix(x):
    return np.array([
        [5 + 20 / (x[0] * np.log(10)), -6],
        [2, 1 - 10 / (x[1] * np.log(10))]
    ])

x0 = [1.0, 1.0]

solution = newton_method(system_equations, jacobian_matrix, x0)
print("Розв'язок методом Ньютона після 2 ітерацій: x =", solution[0], ", y =", solution[1])
