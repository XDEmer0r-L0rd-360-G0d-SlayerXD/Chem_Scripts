K = 273  # set to 0 to remove conversions and assume already celcius


def equi_temp(m1, c1, ts1, m2, c2, ts2):
	# Assumes celcius
	# Solves for Tf of both objects
	return (m1*c1*(ts1+K)+m2*c2*(ts2+K))/(m1*c1+m2*c2)


def mcat(m, c, ts, tf):
	# Assumes celcius
	# Solves for q
	return m*c*(tf-ts)


things = (mcat(500, 2.06, -50, 0), 500*333, mcat(500, 4.184, 0, 100), 500*2256, mcat(500, 1.86, 100, 200))
two = (75.5*333, mcat(75.5, 4.184, 0, 100), 75.5*2256)
print(mcat(1.161*10**3, 4.184, 22.7, 25.06) + mcat(1, 896.9, 22.7, 25.06))
# print((2*(-296.8)+2*(-285.8))-(2*(-20.6)))
# print((2*(-285.8)+180.8)/2)
# print(sum(two))
