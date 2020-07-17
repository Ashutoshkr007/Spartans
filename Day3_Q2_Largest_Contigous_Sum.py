def getMax(arr):
    summax = 0
    curr_sum = 0
    for i in arr:
        curr_sum += i
        if curr_sum < 0:
            curr_sum = 0
        print(curr_sum)
        summax = max(summax, curr_sum)
    return summax


arr = list(map(int, input("Enter a series of num").split()) )
print(arr)
print(getMax(arr))
