'''
    Input: n- nr de semiplane
    semiplanul i (ai, bi, ci) - aix+ biy + ci <=0
    Output: natura intersectiei-vida, nevida si nemarginita, nevida si marginita
    Alg liniar

    Input1:
3
1 0 -1
-1 0 2
0 1 3
    Output1: intersectia este vida

    Input2:
3
-1 0 1
1 0 -2
0 1 3
    Output2: intersectia este nevida,nemarginita

    Input3:
4
-1 0 1
1 0 -2
0 1 3
0 -2 -8
    Output3:intersectia este nevida, marginita

'''

def intersectie(semiplane):
    maximX, maximY = 9999999999, 9999999999
    minimX, minimY = -9999999999, -9999999999

    for semiplan in semiplane:
        Stanga = -9999999999
        Dreapta = 9999999999
        if semiplan[0] == 0: # este semiplan vertical
            if semiplan[1] < 0:
                Stanga = -1* semiplan[2] / semiplan[1]
            else:
                Dreapta = -1* semiplan[2] / semiplan[1]

        else: # este semiplan orizontal
            if semiplan[0] < 0:
                Stanga = -1 * semiplan[2] / semiplan[0]
            else:
                Dreapta = -1 * semiplan[2] / semiplan[0]

        if semiplan[0] == 0: # este semiplan vertical
            minimY = max(minimY, Stanga)
            maximY = min(maximY, Dreapta)
        else: # este semiplan orizontal
            minimX = max(minimX, Stanga)
            maximX = min(maximX, Dreapta)

    if minimY > maximY or minimX > maximX:
        return 0 # intersectie vida
    if (minimX != -9999999999 and maximX != 9999999999) and (minimY != -9999999999 and maximY != 9999999999):
        return 1 # intersectia nevida, marginita
    return 2 # intersectia nevida, nemarginita


semiplane = []
f = open ("7_input_ex1.txt")
n = int(f.readline())
for i in range (n):
    line=f.readline()
    v=line.split()
    semiplan=(float(v[0]), float(v[1]), float(v[2]))
    semiplane.append(semiplan)

output = intersectie(semiplane)
if output== 0:
    print("intersectia este vida")
elif output == 1:
    print("intersectia este nevida, marginita")
else:
    print("intersectia este nevida, nemarginita")