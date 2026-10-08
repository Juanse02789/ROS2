import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# -----------------------------
# EJEMPLO
# -----------------------------

# A = sacar un número par
A = {2, 4, 6}

# B = sacar un número mayor que 3
B = {4, 5, 6}

# Intersección
interseccion = A & B

print("A =", A)
print("B =", B)
print("A ∩ B =", interseccion)

# Probabilidades
P_A = len(A) / 6
P_B = len(B) / 6
P_AB = len(interseccion) / 6

P_A_dado_B = P_AB / P_B

print("\nP(A) =", P_A)
print("P(B) =", P_B)
print("P(A ∩ B) =", P_AB)
print("P(A | B) =", P_A_dado_B)

# -----------------------------
# DIAGRAMA
# -----------------------------

venn = venn2([A, B], set_labels=("A", "B"))

plt.title("Probabilidad condicional")
plt.show()