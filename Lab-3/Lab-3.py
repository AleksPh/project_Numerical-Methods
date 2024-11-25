import numpy as np

A = np.array([[5, 0, 2, 1],
              [0, 4, 0, 1],
              [2, 0, 2, 0],
              [1, 1, 0, 3]], dtype=float)

def power_method_inverse(A, num_iter=5):
    n = A.shape[0]
    x = np.random.rand(n)
    for _ in range(num_iter):
        x = np.linalg.solve(A, x)  
        x = x / np.linalg.norm(x)
    eigval_min = 1 / np.dot(x, A @ x)
    return eigval_min

def jacobi_method(A, num_iter=5):
    n = A.shape[0]
    V = np.eye(n)  
    for _ in range(num_iter):
       
        i, j = np.unravel_index(np.abs(np.triu(A, 1)).argmax(), A.shape)
        if A[i, j] == 0:
            break
        phi = 0.5 * np.arctan2(2 * A[i, j], A[i, i] - A[j, j])
        
        R = np.eye(n)
        R[i, i] = R[j, j] = np.cos(phi)
        R[i, j] = -np.sin(phi)
        R[j, i] = np.sin(phi)
        A = R.T @ A @ R  
        V = V @ R  
    eigenvalues = np.diag(A)
    return eigenvalues


eigval_min = power_method_inverse(A)
eigenvalues_jacobi = jacobi_method(A)

print("Найменше власне значення (степеневий метод):", eigval_min)
print("Власні значення (метод Якобі):", eigenvalues_jacobi)


from sympy import symbols, Eq, diff, log, Matrix, lambdify


x, y = symbols('x y')
f1 = 5*x - 6*y + 20*log(x) + 16
f2 = 2*x + y - 10*log(y) - 4


J = Matrix([[diff(f1, x), diff(f1, y)],
            [diff(f2, x), diff(f2, y)]])

x_k, y_k = 1.0, 1.0
num_iter = 2


for i in range(num_iter):
    J_inv = J.subs({x: x_k, y: y_k}).inv()
    F_k = Matrix([f1, f2]).subs({x: x_k, y: y_k})
    delta = J_inv @ F_k
    x_k, y_k = (Matrix([x_k, y_k]) - delta).evalf()

print(f"Розв'язок методом Ньютона після {num_iter} ітерацій: x = {x_k}, y = {y_k}")
