

def genBin(n):
    arr = []
    k = 0
    while n >= 1:
        if len(arr) < k:
            arr.append(0)
        if pow(2, k) >= n:
            if pow(2, k) > n:
                k -= 1
            else:
                arr.append(0)
            x = pow(2, k)
            n -= x
            arr[k] = 1
            d = k
            k = 0
        k += 1
    return arr

def isPower(num):
    n = int(num)
    comp = []
    xor = []

    arr = genBin(n)
    print("Binary of given no. is:", arr[::-1])

    for i in range(len(arr)):
        comp.append(0)
    print("X-OR comparison array :", comp)

    for i in range(len(arr)):
        xor.append(0)
        xor[i] = (arr[i] + comp[i]) % 10
    print("result of X-OR        :", xor[::-1])

    result = xor.count(1)

    if result == 1:
        print("a perfect power of 2 is " + str(num) + " with power :", d)
    else:
        print(num, "is not a square of of 2", end='')
        if arr[0] == 1:
            print(" and is not divisible by 2")
        else:
            print(" but it is divisible by 2")


num = int(input("Enter a no.: "))
isPower(num)