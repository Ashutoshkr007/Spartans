
a = int(input("Enter a no.       : "))
c = a
a = bin(a)
a = a[2:]
b = int(input("Enter one more no.: "))
d = b
b = bin(b)
b = b[2:]
if len(a) < len(b):
    a = a[::-1]
    for i in range(len(a), len(b) + 1):
        a = a + '0'
    a = int(a[::-1])
elif len(a) > len(b):
    b = b[::-1]
    for i in range(len(b), len(a)):
        b = b + '0'
    b = int(b[::-1])
k = bin(d ^ 0)[2:]
k = k[::-1]

if k.count('1') == 1:
    shift = k.index('1')
    print(c.__rshift__(shift))
else:
    print("The divisor must be a power of 2")
