'''
Dima Oana-Teodora 241.1
    Montonia unui poligon in rap cu axele de coordonate
    Input: n varfuri, P1, P2, ..,Pn
    Output: x-monoton sau y-monoton
    ex Set1: Poligonul nu este x-monoton.Poligonul este y-monoton.
    Complexitate timp O(n)
Set 2 de date de intrare:
8
8 7
7 5
4 5
3 9
0 1
5 2
3 3
10 3
Output: Poligonul nu este x-monoton.Poligonul nu este y-monoton.
'''
# -----Citire Input-----
f=open("6_ex2.txt")
n=int(f.readline())
points=[]
for i in range(n):
    line=f.readline()
    v=line.split()
    x=float (v[0])
    y=float (v[1])
    points.append((x,y))

# -----------Functii ajutatoare-------------------------
def monotony(n,points, axis):
    minimum = points[0][axis]
    position = 0
    for i in range(1,n):
        if points[i][axis] < minimum: # calculez axis-ul cel mai mic
            minimum =points[i][axis]
            position = i

    rising = True # presupun ca este in crestere
    last_point = points[position][axis] # plec de la punctul cu valoarea cea mai mica a axis
    for j in range(1, n):
        current = points[(j + position) % n][axis]
        if current < last_point:
            rising = False # scadere a valorilor => descrestere

        if current > last_point and not rising:
            return False # crestere a valorilor dar nu are un precedent de crestere
        last_point = current

    return True
# -----------Prelucrare date------------------------
x_mon = monotony(n,points,0)

if x_mon:
    print("Poligonul este x-monoton. ", end="")
else:
    print("Poligonul dat nu este x-monoton. ", end="")

y_mon = monotony(n,points,1)
if y_mon:
    print("Poligonul este y-monoton.")
else:
    print("Poligonul dat nu este y-monoton.")
