ele = {"C": 12.01, "O": 16, "H": 1}

def expand_molecule(molecule: str):
	last = ""
	out = ""
	global_mult = 1
	for a in molecule:
		if last == "":
			try:
				global_mult = int(a)
			except:
				out += a
				last = a
		else:
			try:
				out += last * (int(a) - 1)
			except:
				out += a
				last = a
	return out

def mol_mass(molecule: str):
	fixed = expand_molecule(molecule.upper())
	count = 0
	for a in fixed:
		count += ele[a]
	return count
	

def do_calcs():
	# for burning CxHy with only CO2 and H2O
	co2g = 13.65
	h2og = 5.588
	sw = 4.35
	co2m = co2g / mol_mass("co2")
	h2om = h2og / mol_mass('h2o')
	cm = co2m
	hm = h2om * 2
	cg = cm * mol_mass('c')
	hg = hm * mol_mass('h')
	og = sw - cg - hg
	om = og / mol_mass('o')
	print(f"starting => total: {sw}, CO2g: {co2g}, H2O: {h2og}")
	print(f"moles => CO2: {co2m}, H2O: {h2om}, C: {cm}, H: {hm}")
	print(f"grams => C: {cg}, H: {hg}, O: {og}")
	print(f"moles => O: {om}, C{round(cm, 3)}H{round(hm, 3)}O{round(om, 3)}")
	

	
	
def main():
	do_calcs()


	

main()
