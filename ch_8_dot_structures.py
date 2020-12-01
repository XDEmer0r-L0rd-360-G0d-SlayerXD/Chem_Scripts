import string

# Using extra () in formulas is extremely risky and still has bugs

class Element:

    def __init__(self, name, full_name, num, mass, valence):
        self.name = name
        self.full_name = full_name
        self.num = num
        self.mass = mass
        self.valence = valence

    def mass_to_moles(self, mass):
        return mass/self.mass

    def moles_to_mass(self, moles):
        return moles*self.mass

    def formal_charge(self, lone_electrons, bonded_electrons=-1):
        if bonded_electrons == -1:
            return self.valence - (lone_electrons + (8-lone_electrons)/2)
        return self.valence - (lone_electrons + bonded_electrons/2)


class PTable:
    """
    This will only deal in str formulas
    """
    def __init__(self):
        self.H = Element("H", "hydrogen", 1, 1.0078, 1)
        self.He = Element("He", "helium", 2, 4.003, 2)
        self.B = Element("B", "boron", 5, 10.806, 3)
        self.C = Element("C", "carbon", 6, 12.009, 4)
        self.N = Element("N", "nitrogen", 7, 14.006, 5)
        self.O = Element("O", "oxygen", 8, 15.999, 6)
        self.F = Element("F", "fluorine", 9, 18.998, 7)
        self.Ne = Element("Ne", 'neon', 10, 20.18, 8)
        self.Na = Element("Na", "sodium", 11, 22.990, 1)
        self.Si = Element("Si", 'silicon', 14, 28.084, 4)
        self.P = Element("P", "phosphorus", 15, 30.974, 5)
        self.S = Element("S", "sulfur", 16, 32.059, 6)
        self.Cl = Element("Cl", "chlorine", 17, 35.446, 7)
        self.Ar = Element("Ar", 'argon', 18, 39.948, 8)
        self.Ca = Element("Ca", 'calcium', 20, 40.078, 2)
        self.Fe = Element("Fe", 'iron', 26, 55.845, 2)
        self.Ni = Element("Ni", 'nickel', 28, 58.693, 2)
        self.As = Element("As", "arsenic", 33, 74.922, 5)
        self.Se = Element("Se", "selenium", 34, 78.96, 6)
        self.Br = Element("Br", "bromine", 35, 79.904, 7)
        self.Kr = Element("Kr", "krypton", 36, 83.798, 8)
        self.I = Element("I", "iodine", 53, 126.9, 7)
        self.Xe = Element("Xe", "xenon", 54, 131.29, 8)
        self.Hg = Element("Hg", 'mercury', 80, 200.59, 2)

    def total_valence(self, formula):
        split = split_formula(formula)
        total = 0
        for a in split:
            total += self.__getattribute__(a).valence
        return total

    def test_max_valence(self, formula, core):
        # test if there are enough electrons by single bonding all with the core and then maxing out the electrons for each outside
        valence = self.total_valence(formula)
        fixed = split_formula(formula)
        fixed.remove(core)

        valence -= 2 * len(fixed)  # bonds

        temp = []
        for a in fixed:
            if a != "H":
                temp.append(a)
            pass
        fixed = temp

        valence -= 6 * len(fixed)  # lone pairs
        return valence

    def molar_mass(self, formula):
        split = split_formula(formula)
        total = 0
        for a in split:
            total += self.__getattribute__(a).mass
        return total



def split_formula(formula: str):
    def fix_lower(dirty):
        temp = []
        for a in dirty:
            if a in string.ascii_lowercase:
                temp[-1] = temp[-1] + a
            else:
                temp.append(a)
        return temp

    out = []
    if len(formula) == 0:
        return out
    # cant be more than 1 digit long multiplier
    grand_mult = int(formula[0]) if formula[0] in string.digits else 1
    if grand_mult != 1:
        formula = formula[1:]
    formula = formula.split("(")
    if len(formula) == 1:
        for a in fix_lower(list(formula[0])):
            if a in string.digits:
                out.extend([out[-1]]*(int(a) - 1))
            else:
                out.append(a)
        return fix_lower(out)*grand_mult
    for a in formula:
        if ")" in a:
            temp = a.split(")")
            for num_b, b in enumerate(temp):
                if num_b + 2 <= len(temp):
                    temp[num_b] = temp[num_b + 1][0] + temp[num_b]
            val = []
            for b in temp:
                val.extend(split_formula(b))
            out.extend(val)
        else:
            out.extend(split_formula(a))
    return fix_lower(out)


def main():
    table = PTable()
    formula = "OOO"
    extra_electrons = 0
    print(table.total_valence(formula) + extra_electrons)
    print(table.test_max_valence(formula, formula[0:2 if formula[1] in string.ascii_lowercase else 1]) + extra_electrons)
    # print(table.O.formal_charge(6))
    # print(2*413+745 + 2*463 - 498 - 4*413)

if __name__ == '__main__':
    main()
