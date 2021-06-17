'''
Convex Hall -Acoperire convexa
 Input: n - nr varfuri
        P1 P2 .. Pn - varfurile (xi, yi)
 Output: varfurile acoperirii convexe
 Poligon parcurs in sens trigonometric
 Complexitate de timp O(n)
'''
def det (points):
    #calculez determinantul pt o lista points alcatuita din 3 puncte
    det = points[1][0]*points[2][1] + points[2][0] * points[0][1] + points[0][0] * points[1][1] - points[0][1] * points[1][0] - points[0][0] * points[2][1] - points[1][1] * points[2][0]

    return det
f = open("5_input_ex2.txt")
points=[]
n=int(f.readline())
for i in range (n):
    line=f.readline()
    v=line.split()
    x=int (v[0])
    y=int (v[1])
    points.append((x,y))
L= [points[0], points[1]]

for i in range(2, n):
        L.append(points[i])
        # determinantul se va calcula de la cel mai vechi nod pus la cel mai nou
        while len(L)>2 and det([L[-3], L[-2], L[-1]])<=0: # nu determina un viraj la stanga
            # sterg penultimul punct
            del L[-2]

print("Varfurile acoperii convexe sunt: ", * L)




