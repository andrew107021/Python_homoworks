# S = pi*a*b где a, b -- полуоси эллипса
# Пи константа, следовательно, в данной задаче ею можно пренебречь
# 6*6 > 2.5*10 в примере ошибка

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(ell_lst: list) -> tuple:
    out = sorted([x for x in ell_lst if x[0] != x[1]], key=lambda ell: ell[0] * ell[1])
    return out[-1]


print(*find_farthest_orbit(orbits))
