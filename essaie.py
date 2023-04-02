import streamlit as st
import numpy as np

# interface utilisateur
st.title(':blue[Programmation linéaire avec la méthode des coupes de Gomory]')
st.write("la methodes des coupe de Gomory est une technique de résolution de problèmes d'optimisation linéaire qui permet de renforcer les contraintes en ajoutant des inégalités. Cette technique est particulièrement utile pour résoudre des problèmes d'optimisation en nombres entiers en éliminant les solutions non entières. Le coupe de Gomory a été développé par Ralph E. Gomory dans les années 1950 et reste une technique importante dans la résolution de problèmes d'optimisation linéaire en nombres entiers.")
st.title(':blue[a quoi sert cette app web]')
st.write("Le but de cette application web est de permettre à l'utilisateur de résoudre des problèmes d'optimisation linéaire en nombres entiers en utilisant la méthode des coupes de Gomory. L'utilisateur peut saisir les coefficients des variables, les contraintes et la fonction objectif, puis lancer la résolution. L'application affiche ensuite la solution optimale avec les valeurs des variables et la valeur de la fonction objectif correspondante.")


def simplex_dual_gomory(A, b, c):
    # Resoudre le problème du simplexe primal
    tableau = solve_simplex(A, b, c)
    solution_primal = tableau[:, -1]
    # Verifier si la solution est entiere
    if is_integer(solution_primal):
        return solution_primal
    # Resoudre le probleme du simplexe dual
    tableau_dual = solve_simplex_dual(A, b, c)
    solution_dual = tableau_dual[:, -1]
    # Verifier si la solution est entiere
    if is_integer(solution_dual):
        return solution_dual
    # Sinon, appliquer l'algorithme de Gomory
    solution_gomory = gomory(A, b)
    return solution_gomory

def gomory(A, b):
    # Initialisation du tableau
    # On ajoute la valeur de chaque équation de b à la fin de la ligne correspondante de A
    tableau = [list(row) + [val] for row, val in zip(A, b)]
    m, n = len(A), len(A[0])  # m = nombre de lignes, n = nombre de colonnes

    while True:
        # Trouver la ligne avec une partie fractionnaire dans b
        frac_row = None
        for i in range(m):
            if tableau[i][-1] % 1 != 0:
                frac_row = i
                break
        if frac_row is None:
            # Aucune partie fractionnaire trouvée, la solution est un nombre entier
            break

        # Choisir l'élément pivot
        # On prend la colonne avec la plus petite partie fractionnaire pour l'élément pivot
        pivot_col = min(range(n), key=lambda j: tableau[frac_row][j] % 1)
        pivot_row = None
        min_ratio = float('inf')
        for i in range(m):
            if tableau[i][pivot_col] % 1 != 0:
                ratio = tableau[i][-1] / tableau[i][pivot_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i

        # Effectuer l'opération pivot
        pivot = tableau[pivot_row][pivot_col]
        for j in range(n):
            tableau[pivot_row][j] /= pivot
        tableau[pivot_row][-1] /= pivot
        for i in range(m):
            if i != pivot_row:
                factor = tableau[i][pivot_col]
                for j in range(n):
                    tableau[i][j] -= factor * tableau[pivot_row][j]
                tableau[i][-1] -= factor * tableau[pivot_row][-1]

    # Extraire la solution du tableau
    x = [0] * n
    for i in range(m):
        for j in range(n):
            if tableau[i][j] == 1:
                x[j] = tableau[i][-1]
                break

    # Retourner la solution
    return x

def solve_simplex(A, b, c):
    m, n = A.shape
    tableau = np.hstack((A, b.reshape(-1, 1)))
    tableau = np.vstack((tableau, np.hstack((c.reshape(1, -1), np.zeros((1, 1))))))
    basis = list(range(n, n+m))
    while True:
        col_index = find_entering_variable(tableau[-1, :-1])
        if col_index is None:
            break
        row_index = find_leaving_variable(tableau[:, col_index], tableau[:, -1], basis)
        if row_index is None:
            break
        basis[row_index] = col_index
        tableau[row_index, :] /= tableau[row_index, col_index]
        for i in range(m+1):
            if i != row_index:
                tableau[i, :] -= tableau[i, col_index] * tableau[row_index, :]
    return tableau

def solve_simplex_dual(A, b, c):
    m, n = A.shape
    tableau = np.hstack((A.T, b.reshape(-1, 1)))
    tableau = np.vstack((tableau, np.hstack((c.reshape(1, -1), np.zeros((1, 1))))))
    basis = list(range(n, n+m))
    while True:
        row_index = find_entering_variable(tableau[-1, :-1])
        if row_index is None:
            break
        col_index = find_leaving_variable(tableau[row_index, :-1], tableau[row_index, -1], basis)
        if col_index is None:
            break
        basis[row_index] = col_index
        tableau[:, row_index] /= tableau[col_index, row_index]
        for j in range(n+1):
            if j != row_index:
                tableau[:, j] -= tableau[col_index, j] * tableau[:, row_index]
    return tableau.T

def find_entering_variable(c):
    # Chercher l'indice de la variable entrante
    mask = c < 0
    if mask.any():
        return np.argmin(c)
    return None

def find_leaving_variable(A_col, b, basis):
    # Chercher l'indice de la variable sortante
    mask = A_col > 0
    ratios = np.where(mask, b / A_col, np.inf)
    min_ratio = np.min(ratios)
    if np.isinf(min_ratio):
        return None
    row_index = np.argmin(ratios)
    return basis[row_index]

def is_integer(x):
    # Verifier si tous les elements de x sont entiers
    return np.all(np.isclose(x, np.round(x)))


st.title(':green[Problème d optimisation linéaire en nombres entiers]')

# Définir les variables et la fonction objectif
st.subheader("Définir la fonction objectif")
num_vars = st.number_input("Nombre de variables", min_value=1, value=2)
c = np.zeros(num_vars)
for i in range(num_vars):
    c[i] = st.number_input(f"Coefficient de x_{i+1}", key=f"c{i}")
op = st.radio("Type d'optimisation", ("Maximisation", "Minimisation"))

# Définir les contraintes
st.subheader("Définir les contraintes")
num_cons = st.number_input("Nombre de contraintes", min_value=1, value=2)
A = np.zeros((num_cons, num_vars))
b = np.zeros(num_cons)
for i in range(num_cons):
    for j in range(num_vars):
        A[i, j] = st.number_input(f"Coefficient de x_{j+1} dans la contrainte {i+1}", key=f"a{i}{j}")
    b[i] = st.number_input(f"Terme constant de la contrainte {i+1}", key=f"b{i}")
    op_cons = st.radio(f"Type de la contrainte {i+1}", ("<=", "=", ">="))
    if op_cons == "<=":
        A[i] = -A[i]
    elif op_cons == "=":
        A = np.vstack((A, -A[i]))
        b = np.hstack((b, -b[i]))
    elif op_cons == ">=":
        b[i] = -b[i]

# Calculer la solution
if st.button("Calculer"):
    if op == "Maximisation":
        c = -c
    solution_gomory = gomory(A, b)
    st.write("La solution optimale est", solution_gomory)