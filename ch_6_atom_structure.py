import math

C = 2.998*10**8  # m/s = speed of light
h = 6.626*10**(-34)  # Js
nm = 10**9
pm = 10**12
Rhc = 2.179*10**(-18)  # J/photon
pmol = 6.02*10**23  # 1 mol = pmol photons


def snprint(x):
    print('{:.2e}'.format(x))


def sn(c, e=0):
    return c*10**e


def rhcf(s, e):
    return -Rhc*((1/(e**2)-1/(s**2)))


'''
def learning():
    # val = C/(1.92*10**15)
    # snprint(val)
    # print(val*10**9)

    # val = 450/nm
    # snprint(val)
    # snprint(h*C/val)

    # val = -Rhc*(1/4-1/16)
    # print(C*h/val*nm)

    val = h/(sn(9.11, -31)*sn(1.7, 8))
    snprint(val*pm)


def adaptive():
    snprint((-Rhc*(1/64-1/9)))


def homework():
    snprint(h*C/sn(6.9, -19))
'''

"""
Equations:
w=C/v
E=hv
by extension: E=(hC)/w
E=-Rhc/n^2
dE=-Rhc(1/n_final^2-1/n_initial^2)
1 J = 1 kg m^2 s^-2
when m: kg and v: m/s => w=h/(mv)
"""

def exam():
    print(h/(.14*40.2))

def main():
    # learning()
    # adaptive()
    # homework()
    exam()


if __name__ == '__main__':
    main()
