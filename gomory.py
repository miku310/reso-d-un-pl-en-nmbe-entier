import streamlit as st
st.title("coupe de Gomory")
st.write("la methodes des coupe de Gomory est une technique de résolution de problèmes d'optimisation linéaire qui permet de renforcer les contraintes en ajoutant des inégalités. Cette technique est particulièrement utile pour résoudre des problèmes d'optimisation en nombres entiers en éliminant les solutions non entières. Le coupe de Gomory a été développé par Ralph E. Gomory dans les années 1950 et reste une technique importante dans la résolution de problèmes d'optimisation linéaire en nombres entiers.")
st.title("a quoi sert cette app web:")
st.write("Le but de cette application web est de permettre à l'utilisateur de résoudre des problèmes d'optimisation linéaire en nombres entiers en utilisant la méthode des coupes de Gomory. L'utilisateur peut saisir les coefficients des variables, les contraintes et la fonction objectif, puis lancer la résolution. L'application affiche ensuite la solution optimale avec les valeurs des variables et la valeur de la fonction objectif correspondante.")
# fonction pour résoudre le problème d'optimisation linéaire
def solve_LP(variables, contraintes, obj):
    # code pour résoudre le problème d'optimisation linéaire en nombres entiers
    # ...
    return result

# interface utilisateur
st.title("Problème d'optimisation linéaire en nombres entiers")

# champs pour les coefficients des variables
st.subheader("Coefficients des variables:")
var1 = st.number_input("Variable 1", value=0,min_value=0)
var2 = st.number_input("Variable 2", value=0,min_value=0)
var3 = st.number_input("Variable 3", value=0,min_value=0)

# champs pour les contraintes
st.subheader("Contraintes:")
con1var1 = st.number_input("Contrainte 1 - Variable 1", value=0)
con1var2 = st.number_input("Contrainte 1 - Variable 2", value=0)
con1var3 = st.number_input("Contrainte 1 - Variable 3", value=0)
con1type = st.selectbox("Contrainte 1 - Type", options=["=", "<=", ">="])
con1const = st.number_input("Contrainte 1 - Constant", value=0)

con2var1 = st.number_input("Contrainte 2 - Variable 1", value=0)
con2var2 = st.number_input("Contrainte 2 - Variable 2", value=0)
con2var3 = st.number_input("Contrainte 2 - Variable 3", value=0)
con2type = st.selectbox("Contrainte 2 - Type", options=["=", "<=", ">="])
con2const = st.number_input("Contrainte 2 - Constant", value=0)

# champ pour la fonction objectif
st.subheader("Fonction objectif:")
objvar1 = st.number_input("Variable 1", value=0)
objvar2 = st.number_input("Variable 2", value=0)
objvar3 = st.number_input("Variable 3", value=0)
objtype = st.selectbox("Type", options=["max", "min"])

if st.button("Résoudre"):
    # Afficher le PL entré par l'utilisateur
    st.subheader("Problème d'optimisation linéaire:")
    st.write(objvar1, "x1 +", objvar2, "x2 +", objvar3, "x3",objtype)
    st.write(con1var1, "x1 +", con1var2, "x2 +", con1var3, "x3", con1type, con1const)
    st.write(con2var1, "x1 +", con2var2, "x2 +", con2var3, "x3", con2type, con2const)
    # appel de la fonction qui résoud le problème d'optimisation linéaire
    variables = [var1, var2, var3]
    contraintes = [[con1var1, con1var2, con1var3, con1type, con1const],
                   [con2var1, con2var2, con2var3, con2type, con2const]]
    obj = [objvar1, objvar2, objvar3, objtype]
    result = solve_LP(variables, contraintes, obj)
    
    # affichage des résultats
    st.subheader("Résultat:")
    st.write(result)

