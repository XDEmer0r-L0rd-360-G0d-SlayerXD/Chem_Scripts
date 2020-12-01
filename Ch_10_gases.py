from ch_6_atom_structure import sn, snprint
from ch_8_dot_structures import PTable
import math


# Constants/conversion nums
# 1 atm = 760 mm Hg
hg = torr = 760
pa = 101325
kpa = pa / 1000
bar = 1.01325
mbar = bar * 1000
psi = 14.69
R_pvnrt = .0821
R_gas = 8.314
K = 273
stp_vol = 22.4
stp_t = K
stp_p = 1

# formulas
"""
P=F/A
PV=nRT
PV/(nT)=PV/(nT)
d=PM/(RT): density = pressure*molar mass/(R*temp)
root-mean-square speed = sqrt(3RT/M): R = gas energy constant, M = kg
E_g1/E_g2 = sqrt(mm_g2/mm_g1): mm = molar mass
E_g1^2/mm_g2 = E_g2^2/mm_g1
(P+a*n^2/V^2)(V-nb) = nRT
(P+a/V^2)(V-b) = RT
"""


def conv(celcius=None, kelvin=None):

    if celcius:
        return celcius + K
    return kelvin - K


def io_pvnt(i_p=None, i_v=None, i_n=None, i_t=None, o_p=None, o_v=None, o_n=None, o_t=None):
    if not i_p and not o_p:
        i_p = o_p = 1
    if not i_v and not o_v:
        i_v = o_v = 1
    if not i_n and not o_n:
        i_n = o_n = 1
    if not i_t and not o_t:
        i_t = o_t = 1

    if not o_t:
        print('ot')
        return (i_t * i_n * o_v * o_p) / (i_v * i_p * o_n)
    elif not o_n:
        print("on")
        return (i_t * i_n * o_v * o_p) / (i_v * i_p * o_t)
    elif not o_v:
        print('ov')
        return (i_v * i_p * o_t * o_n) / (i_t * i_n * o_p)
    elif not o_p:
        print('op')
        return (i_v * i_p * o_t * o_n) / (i_t * i_n * o_v)


def pvnrt(p=None, v=None, n=None, t=None):
    # Only the formula, no internal conversions done
    if not p:
        return n*R_pvnrt*t/v
    elif not v:
        return n*R_pvnrt*t/p
    elif not n:
        return p*v/R_pvnrt/t
    elif not t:
        return p*v/R_pvnrt/n


def learning():
    table = PTable()
    # d=PM/(RT)
    # (P+a*n^2/V^2)(V-nb) = nRT
    print(pvnrt(None, .5, 9/table.O.mass, 298))


def main():
    learning()


if __name__ == '__main__':
    main()
