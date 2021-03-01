x = input('ποιό αρχείο θες ρε μπροο  ')
file = open(x, 'r')
text = file.read()
a = text.split(' ')
z = len(a) -2
o = len(a)
while True :
    for i in range(z):
        if i < z :
            if len(a[i]) + len(a[i+1]) == 20 :
                print(a[i],a[i+1])
                a.remove(a[i])
                a.remove(a[i+1])
                z -= 2
    if o == len(a) :
        break
    o = len(a)
