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
            k = 0
        k += 1
    return arr

def genSub(arr):
    sub = []
    leng = pow(2, len(arr))
    for i in range(leng):
        x = genBin(i)
        print('{ ', end='')
        if not x:
            print(' ', end='')
        else:
            for i in range(len(x)):
                if x[i] == 1:
                    print(arr[i], "", end='')
        print('}')




arr = input("Enter a set").split(' ')
genSub(arr)
