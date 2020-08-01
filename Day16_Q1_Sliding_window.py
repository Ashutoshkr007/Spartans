def check(new_string, string):
    if string in new_string:
        return 0
    return 1


string = input()
new_string = ''
max_sub = []
i = 0
while i < len(string):
    count = check(new_string, string[i])
    if count:
        new_string += string[i]
        i += 1
    else:
        max_sub.append(new_string)
        new_string = ''
max_sub.append(new_string)
print(max(max_sub))
