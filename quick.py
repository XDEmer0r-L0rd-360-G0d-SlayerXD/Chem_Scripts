import math

data = [(31.82, -13.3), (15.89, -10.58), (7.6, -13.6), (12.2, -8.51)]
for num_a, a in enumerate(data):
	print(f"{num_a}: {math.sqrt((a[1] - a[0])**2/((a[1] + a[0])**2 + (2 * a[0] * a[1])**2))}")