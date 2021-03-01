import random
x = int(input('Δωσε την πρώτη διασταση του ορθογωνίου: '))
y = int(input('Δωσε την δεύτερη διασταση του ορθογωνίου να τελειώνουμε με την πάρτη σου: '))
mylist = ["O", "S"]
a = [[0]*y]*x
sums = 0
sumo = 0
sumorizontia = 0
sumkatheta = 0
sumdiagwnia = 0
for i in range(x):
    for j in range(y):
        a[i][j] = (random.choice(mylist))
        if a[i][j] == 'S' :
            sums += 1
        else :
            sumo += 1
        if sums > (x * y // 2):
            a[i][j] = 'O'
        if sumo > (x * y//2):
            a[i][j] = 'S'

for i in range(x):
    for j in range(y-2):
        if a[i][j] == "S" and a[i][j+1] == "O" and a[i][j+2] == "S" :
            sumorizontia += 1
for i in range(x-2):
    for j in range(y):
        if a[i][j] == "S" and a[i+1][j] == "O" and a[i+2][j] == "S" :
            sumkatheta += 1
for i in range(x-2) :
    for j in range(y-2):
        if a[i][j] == "S" and a[i+1][j+1] == "O" and a[i+2][j+2] == "S" :
            sumdiagwnia += 1
for i in range(x-2) :
    for j in range(2,y) :
        if a[i][j] == "S" and a[i+1][j-1] == "O" and a[i+2][j-2] == "S" :
            sumdiagwnia += 1
S = sumorizontia + sumkatheta + sumdiagwnia
if S == 0 :
    print('SOS οριζόντια' , sumorizontia)
    print('SOS κάθετα' , sumkatheta)
    print('SOS διαγώνια' , sumdiagwnia)
else :
    print('SOS οριζόντια' , sumorizontia / S *100 , '%')
    print('SOS κάθετα' , sumkatheta / S *100 , '%')
    print('SOS διαγώνια' , sumdiagwnia / S *100 , '%')
