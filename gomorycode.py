import streamlit as st

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

# Exemple d'utilisation
A = [[1, 1, 1], [2, 1, 0], [0, 2, 1]]
b = [5, 8, 6]
x = gomory(A, b)

st.write("Solution :", x) # affiche la solution calculée par la fonction gomory




import streamlit as st

def gomory(A, b):
    # Initialise le tableau en concaténant chaque ligne de A avec l'élément correspondant de b
    tableau = [list(row) + [val] for row, val in zip(A, b)]
    m, n = len(A), len(A[0])

    while True:
        # Trouve la ligne i avec une partie fractionnaire dans b
        frac_row = None
        for i in range(m):
            if tableau[i][-1] % 1 != 0:
                frac_row = i
                break
        if frac_row is None:
            # Aucune partie fractionnaire trouvée, la solution est entière
            break

        # Choisissez l'élément pivot
        pivot_col = min(range(n), key=lambda j: tableau[frac_row][j] % 1)
        pivot_row = None
        min_ratio = float('inf')
        for i in range(m):
            if tableau[i][pivot_col] % 1 != 0:
                ratio = tableau[i][-1] / tableau[i][pivot_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i

        # Effectue l'opération de pivot
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

    # Extrait la solution du tableau
    x = [0] * n
    for i in range(m):
        for j in range(n):
            if tableau[i][j] == 1:
                x[j] = tableau[i][-1]
                break

    # Retourne la solution
    return x


# Exemple d'utilisation
A = [[1, 1, 1], [2, 1, 0], [0, 2, 1]]
b = [5, 8, 6]
x = gomory(A, b)
st.write("Solution :", x)