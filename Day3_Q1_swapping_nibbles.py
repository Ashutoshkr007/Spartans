def binGen(num):
    arr = []
    k = 0
    required = 8
    while num >=1:
        if len(arr) < k:
            arr.append(0)
        if pow(2, k)>= num:
            if pow(2, k) > num:
                k -= 1
            x = pow(2, k)
            num -= x
            arr[k] = 1
            k = 0
        k += 1
    if len(arr) < required:
        while len(arr) < required:
            arr.append(0)
    return arr

def genDec(binNum):
    dnum = 0
    for i in range(len(binNum)):
        x = pow(2, i)
        dnum += x * binNum[i]
    print(dnum)

num = int(input("Enter a num"))
binNum = binGen(num)
print(binNum)
binNum = binNum[4:] + binNum[:4]
print(binNum)
genDec(binNum)


