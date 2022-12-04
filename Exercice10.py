def aux(lg, L, dec, Lcop, step=[]):
    if len(L) == 0:
        if len(step) != 0 and lg < Lcop:
            dec.append(step[:])
        return
    j = 0
    tmp = lg
    while tmp >= 0:
        step.append(j)
        aux(tmp, L[1:], dec, L[0], step)
        step.pop()
        tmp -= L[0]
        j += 1


def alumBarre(lg, L):
    dec = []
    aux(lg, L, dec, L[0])
    return dec


dec = alumBarre(500, [200, 120, 100, 50])
print(dec)
