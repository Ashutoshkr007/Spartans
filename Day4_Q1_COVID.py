def neighbours(age, infected):
    subAge = []
    patients = []
    i = 0
    x = 0
    i_min = 0
    i_max = 5
    for i in range(i_min, i_max):
        if age[i].__contains__(infected):
            x = age[i].index(infected)
            break

    patients.append(infected)
    if age[i][x] == infected:
        print(infected)
    age[i][x] = 20
    i_min = i - 1
    i_max = i + 2
    if i_min < 0:
        i_min = 0
    if i_max > 5:
        i_max = 5
    j_min = x - 1
    j_max = x + 2
    if j_min < 0:
        j_min = 0
    if j_max > 4:
        j_max = 4

    for t in range(i_min, i_max):
        subAge.append(age[t][j_min:j_max])
    i = 0
    while i < len(subAge):
        for j in range(0, len(subAge[i])):
            if subAge[i][j] > 50:
                neighbours(age, subAge[i][j])
            elif subAge[i][j] < 18:
                neighbours(age, subAge[i][j])
        i+= 1
    return patients


newInfect = []
age = []
i = 0
print("Enter the ages acc. to beds")
for i in range(5):
    age.append(list(map(int, input().split())))
print(age)
x = 0
infected = int(input("\nEnter  the age of the person infected"))

newInfect = neighbours(age, infected)

