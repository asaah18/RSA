file = open("encryption.txt", "r")
x = file.readlines()
print(x)
for y in x:
        y = ord(y) #converts character into ASCII reference number
        y = (y ** e) % n #encrypts using rsa algorithm
        x = chr(y)
        newx +=  y
print(y)
file.close()

file = open("encryption.txt", "r")
x = file.read()

i=0
while i < len(x):
    print(x[i])
    i=i+1


file.close()
