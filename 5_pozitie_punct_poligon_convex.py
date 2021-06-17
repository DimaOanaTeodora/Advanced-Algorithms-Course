'''
 Stabilirea pozitiei unui punct fata de un poligon complex
 Input: n - nr varfuri
        P1 P2 .. Pn - varfurile (xi, yi)
 Output: pozitia relativa a unui punct Q fata de poligon -> in interior/exterior, pe laturi
 Poligon parcurs in sens trigonometric
 O(log N)
'''

f = open("5_input_ex3.txt")
points=[]
n=int(f.readline())
for i in range (n):
    line=f.readline()
    v=line.split()
    x=int (v[0])
    y=int (v[1])
    points.append((x,y))
# citire punct q
line=f.readline()
v=line.split()
x=int (v[0])
y=int (v[1])
q=(x,y)

# -------------------------------------------------

def cross1(p1, p2):
    #produs incrucisat
    #punctul de afla intre p1 si pn => cross1 ==0
    return p1[0]*p2[1]-p1[1]*p2[0]

def cross2(p1, p2, p3):
    return cross1((p2[0] - p1[0], p2[1] - p1[1]),(p3[0] - p1[0], p3[1] - p1[1]))


def sgn(val):
    #stabilesc daca este in dreapta, stanga , coliniar
    if val == 0:
        # punctul este coliniar
        return 0
    elif val> 0:
        #punctul este in dreapta
        return 1
    else:
        # punctul este in stanga
        return -1


def pointInTriangle(p1, p2, p3, p):
    #verific daca se afla in interiorul triunghiului det de p1,p2,p3
    s1 = abs(cross2(p1, p2,p3))
    s2 = abs(cross2(p, p1, p2)) + abs(cross2(p,p2, p3)) + abs(cross2(p,p3, p1))
    return s1 == s2

def pointInConvexPolygon(points,point, n):
    #rezultatul unei interogari
    #points vine din pepare()
    if cross1(points[0],point) != 0 and sgn(cross1(points[0],point)) != sgn(cross1(points[0],points[n - 1])):
        return False
    if cross1(points[n-1],point) != 0 and sgn(cross1(points[n-1],point)) != sgn(cross1(points[n-1],points[0])):
        return False
    #cazul special in care punctul se afla pe un segment
    if cross1(points[0],point) == 0:
        return points[0][0]*points[0][1] >= point[0]*point[1]

    left = 0
    right = n - 1
    #cautare binara
    # astfel incat punctul sa nu fie in sens invers acelor de ceasornic

    while(right-left > 1):
        mid = (left + right)//2
        pos = mid
        if cross1(points[pos],point) >= 0:
            left = mid
        else:
            right = mid

    pos = left
    return pointInTriangle(points[pos], points[pos + 1], (0, 0), point)


if pointInConvexPolygon(points, q , n) == True:
    print("Punctul Q="+ str(q)+ " se afla in interiorul poligonului")
else:
    print("Punctul Q="+ str(q)+ " se afla in exteriorul poligonului")
