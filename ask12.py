x = input('ποιό αρχείο θεσ ρε μπροο')
file = open(x, 'r')
text = file.read()
a = f'List of Characters ={list(text.strip())}'
b = [0]*len(a)
c = [0]*len(a)
d = [0]*len(a)
print(len(a))
for i in range(len(a)) :
    b[i] = ord(a[i])
    c[i] = chr(127 - b[i]) #128
for i in range(len(a)):
    d[100 - i] =  c[i]
print(d)
