'''
    Pozitia unui punct fata de semiplane orizontale si verticale.
    Input:
    punctul Q
    n- nr de semiplane
    semiplanul i (ai, bi, ci) - aix+ biy + ci <=0
    Output: exista un dreptunghi cu proprietatea ceruta, valoarea minima a
ariilor dreptunghiurilor cu proprietatea ceruta este Z
    Alg liniar

    Input1:
1.5 4
3
-1 0 1
1 0 -2
0 1 3
    Output1: nu exista un dreptunghi cu proprietatea ceruta

    Input2:
0 0
4
-1 0 1
1 0 -2
0 1 3
0 -2 -8
    Output2: nu exista un dreptunghi cu proprietatea ceruta

    Input3:
1.25 -3.5
4
-1 0 1
1 0 -2
0 1 3
0 -2 -8
    Output3:exista un dreptunghi cu proprietatea ceruta, valoarea minima a
ariilor dreptunghiurilor cu proprietatea ceruta este 1.

    Input4:
2 1
11
-1 0 -1
0 -3 -6
0 2 -6
1 0 -3
0 1 -2
2 0 -10
0 -1 -3
-4 0 0
-1 0 1
0 -1 -1
1 0 -4
    Output4:exista un dreptunghi cu proprietatea ceruta, valoarea minima a
ariilor dreptunghiurilor cu proprietatea ceruta este 6

'''

def intersectie(semiplane, Q):
    maximX, maximY = 9999999999, 9999999999
    minimX, minimY = -9999999999, -9999999999

    for semiplan in semiplane:
        if semiplan[0] == 0:  # este semiplan vertical
            if (semiplan[2]+ semiplan[1] * Q[1] ) >= 0:
                continue
        else:  # este semiplan orizontal
            if (semiplan[2] + semiplan[0] * Q[0] ) >= 0:
                continue

        if semiplan[0] == 0:  # este semiplan vertical
            if -1 * semiplan[2] / semiplan[1] < Q[1]:
                minimY = max(minimY, -1 * semiplan[2] / semiplan[1])
            else:
                maximY = min(maximY, -1 * semiplan[2] / semiplan[1])
        else:  # este semiplan orizontal
            if -1 * semiplan[2] / semiplan[0] < Q[0]:
                minimX = max(minimX, -1 * semiplan[2] / semiplan[0])
            else:
                maximX = min(maximX, -1 * semiplan[2] / semiplan[0])

    if  max(maximX, maximY) == 9999999999 or min(minimX, minimY) == -9999999999 :
        return 0 # nu exista dreptunghiuri
    return (maximX - minimX) * (maximY - minimY) # calculez valoarea ariilor

semiplane = []
f = open ("7_input_ex2.txt")
line = f.readline()
v = line.split()
Q = (float(v[0]), float(v[1]))

n = int(f.readline())
for i in range (n):
    line=f.readline()
    v=line.split()
    semiplan=(float(v[0]), float(v[1]), float(v[2]))
    semiplane.append(semiplan)

output = intersectie(semiplane, Q)

if output == 0:
    print("nu exista dreptunghi cu proprietatea ceruta")
else:
    print("exista un dreptunghi cu proprietatea ceruta, valoarea minima a ariilor dreptunghiurilor cu proprietatea ceruta este " + str(output))