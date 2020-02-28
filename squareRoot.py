def setKnownRoots(rootDict):
    rootDict[1] = 1
    rootDict[4] = 2
    rootDict[9] = 3
    rootDict[16] = 4
    rootDict[25] = 5
    rootDict[36] = 6
    rootDict[49] = 7
    rootDict[64] = 8
    rootDict[81] = 9
    rootDict[100] = 10
    rootDict[225] = 15
    rootDict[400] = 20
    rootDict[10000] = 100


def getStartingIntervall(num):
    if (num < 100):
        v1 = 0
        d1 = 100
        v2 = 0
        d2 = 100
        # TODO: this might be solved smarter with another recursive function
        # that doesn't have to iterate over the whole list since it is already sorted
        for number, root in knownRoots.items():
            distance = abs(num - number)
            if (distance < d1):

                if (d1 < d2):
                    d2 = d1
                    v2 = v1

                d1 = distance
                v1 = root

            elif (distance < d2):
                d2 = distance
                v2 = root
        # the way the check works the first number will always be closer to the result than the second
        # can I make use of that for improving the algorithm?
        # for the split approach the list has to be sorted by value and not by distance
        if (v1 > v2):
            return [v2, v1]

        return [v1, v2]

    # TODO: find better starting intervals for numbers > 100
    return [10, num]


def splitInterval(num, invl, i):

    # Intervalberechnung durch Aufteilung => ca. 10 - 25 iterationen
    # Erfordert sortiertes Array!
    invlRange = invl[1] - invl[0]
    if (invlRange < 0.0001):
        print(i)
        return (invl[0] + invl[1])/2

    _i = i+1
    middle = invl[0] + (invlRange / 2)

    print(middle)
    leftInvl = [invl[0], middle]
    rightInvl = [middle, invl[1]]

    if ((middle**2) > num):
        return splitInterval(num, leftInvl, _i)

    return splitInterval(num, rightInvl, _i)


def calcNextInterval(num, invl, i):
    # Intervallberechnung mit linearer Distanz -> ca. 30 Iterationen im zweistellingen bereich
    # Mehr als ca. 200 iterationen bei num > 100 / exceed bei 1000!

    # Abbruchbedingung
    if (abs(invl[1] - invl[0]) < 0.001):
        print(i)
        return (invl[0] + invl[1])/2

    _i = i+1
    sqr1 = invl[0]**2
    sqr2 = invl[1]**2

    d1 = sqr1 - num
    d2 = sqr2 - num

    n1 = invl[0] - d1/sqr1
    n2 = invl[1] - d2/sqr2

    return calcNextInterval(num, [n1, n2], _i)


def getRoot(num):

    if (num.is_integer() and num in knownRoots):
        return knownRoots[num]
    else:
        i = 0
        interval = getStartingIntervall(num)
        print(interval)
        return splitInterval(num, interval, i)


knownRoots = dict()
setKnownRoots(knownRoots)
number = float(input())
res = getRoot(number)
print(res)
