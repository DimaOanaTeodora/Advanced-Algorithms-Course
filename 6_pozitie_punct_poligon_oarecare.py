'''
Dima Oana-Teodora 241.1
    Input: n varfuri, P1, P2, ..,Pn si Q
    Output: pozitia lui Q fata de poligon : in interior, in exterior, pe laturi
    Algoritm liniar
    ex: Q(3,4) interior; Q(7,3) exterior; Q(3,2) pe laturi
'''
import math
# -----Citire Input-----
f=open("6_ex1.txt")
n=int(f.readline())
points=[]
for i in range(n):
    line=f.readline()
    v=line.split()
    x=float (v[0])
    y=float (v[1])
    points.append((x,y))
line=f.readline()
v=line.split()
x=float (v[0])
y=float (v[1])
Q=(x,y)

#-----------Functii ajutatoare-------------------------

# calculez panta (inclinarea segmentului determinat de punctele p1 si p2
def orientation(p1, p2):
    if p2[0] - p1[0] != 0: # ca sa evit impartirea la 0
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    return 0 # daca punctele coincid 

# calculez determinantul pt o lista points alcatuita din 3 puncte
def determinant (points):
    det = points[1][0]*points[2][1] + points[2][0] * points[0][1] + points[0][0] * points[1][1] - points[0][1] * points[1][0] - points[0][0] * points[2][1] - points[1][1] * points[2][0]
    return det

def sgn(p1, p2, p3):
    det = determinant([p1,p2,p3])
    # stabilesc daca este in dreapta, stanga , coliniar
    if det == 0:
        # punctul este coliniar
        return 0
    elif det > 0:
        # punctul este in dreapta
        return 1
    else:
        # punctul este in stanga
        return -1

# verifica daca un punct p3 este pe p1p2
def on_segment(p1, p2, p3):
    # trebuie sa aiba ori acelasi x ori acelasi y
    if p1[0]==p2[0]==p3[0] or p1[1]==p2[1]==p2[3]:
        return True
    return False

def intersect(p1,p2, q1,q2):

        if orientation(p1,p2)== orientation(q1,q2):
            #p1p2 si q1q2 sunt paralele si nu se pot intersecta
            return False

        # vad pozitiile punctelor
        position1 = sgn(p1,p2,q1)
        position2 = sgn(p1,p2,q2)
        position3 = sgn(q1,q2,p1)
        position4 = sgn(q1,q2,p2)
        # position ==0 => punctul este coliniar

        if (position1 == position2) or (position3 == position4):
            #q1==q2 sau p1==p2
            return True
        if (position1 == 0) and on_segment(p1,q2,p2):
            # p1,p2,q1 sunt coliniare
            # p2 e pe segmentul p1q2

            return True
        if (position2 == 0) and on_segment(p1,q2,p2):
            # p1,p2,q2 coliniare
            # p2 pe segmentul p1q2

            return True
        if (position3 == 0) and on_segment(q1,p1,q2):
            # q1,q2,p1 sunt coliniare
            # q2 pe segmentul q1,p1,

            return True
        if (position4 == 0) and on_segment(q1,p2,q2):
            # q1,q2,p2 coliniare
            # q2 pe segmentul q1,p2
            return True

        return False
def check_position(n,points, Q):

    end = (100000, 100000) # iau ca o limita superioara
    nr_intersec = 0

    for i in range(n):
        if i==n-1:
            p = points[0]
        else:
            p = points[i + 1]
        if sgn(points[i], p, Q) == 0: # Q se afla pe latura poligonului
            return 0
        elif intersect(points[i], p, Q, end):
            nr_intersec += 1

    if nr_intersec % 2 == 0: # Q se afla in exteriorul poligonului
        return -1
    return 1 # Q se afla in interiorul poligonului

#-----------Prelucrare date------------------------
pos = check_position(n,points, Q)
if pos == 1:
    print("Punctul",Q,"se afla in interiorul poligonului")
elif pos == -1:
    print("Punctul",Q,"se afla in exteriorul poligonului")
else:
    print("Punctul",Q,"se afla pe latura poligonului")
