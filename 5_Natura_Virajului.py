'''
 Input: 3 puncte P,Q,R din R^2
 Output: natura virajului PQR, viraj stanga, viraj dreapta, puncte coliniare
    Determinantul:
    1                   1               1
    points[0][0]    points[1][0]    points[2][0]
    points[0][1]    points[1][1]    points[2][1]
'''
f = open("5_input_ex1.txt")
points=[]
for i in range (3):
    line=f.readline()
    v=line.split()
    x=int (v[0])
    y=int (v[1])
    points.append((x,y))

# calculez determinantul
det = points[1][0]*points[2][1] + points[2][0] * points[0][1] + points[0][0] * points[1][1] - points[0][1] * points[1][0] - points[0][0] * points[2][1] - points[1][1] * points[2][0]
if det ==0:
    print("Puncte coliniare")
elif det <0:
    print("Viraj la dreapta")
else:
    print("Viraj la stanga")

