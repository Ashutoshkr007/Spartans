
def NoOf1(num):
    n = int(num)
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
    print("Binary of given no. is:", arr[::-1])

    result = arr.count(1)
    print("Number of 1 in", num, "is", result)


num = int(input("Enter a no.: "))
NoOf1(num)
