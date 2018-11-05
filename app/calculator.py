import math

# Calculation formulas.

# (it is very short descriptions, because we talk about well-known things)
# Denote (units of measurement in brackets):

# m [g] - weight of protein (for example, quantity in microfuge tube) [gram];
# Mw [kDa] - molecular weight of protein [kilo Dalton];
# Q [mol] - quantity of protein (in the same tube) [mole];
# N [pieces] - quantity of protein [pieces];
# c [M] - molar concentration of protein [Mole]=[mole/litre];
# V [L] - dilution volume [litre];
# NA - Avogadro constant = 6.022045x10^23[1/mole];
# the relation between these values will be:

# m[g] = Q[mol] x Mw[kDa] x 10^3
# N[pieces] = Q[mol] x NA
# c[M] x V[L] = Q[mol]


def compute(x):
    return math.sin(x)

def test(x, y):
    return x*y

def protein_weight(Q, Mw):
    return Q*Mw*1000

def protein_quentity(Q):
    NA = 6.02214086*(10**23)
    return Q*NA

def protein_mole(mass, Mw, mass_unit):
    return mass*mass_unit/(Mw*1000)

def protein_molar_conc(mol, V):
    return mol/V

def buffer_mass(Molar, Molar_unit, Vol, Vol_unit, Mw):
    M = float(Molar)*float(Molar_unit)
    V = float(Vol)*float(Vol_unit)
    return (M*V)/Mw