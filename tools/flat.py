def flat(linFac):
    helper = []
    for x in linFac:
        for y in x:
            if type(y) == frozenset:
                for z in y:
                    helper.append(z)

            if type(y) == tuple:
                for z in y:
                    helper.append(z)
            else:
                helper.append(y)
    return helper


def toWords(liste):
    helper = []
    for x in liste:
        helper.append(x.getName())
    return helper
