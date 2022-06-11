s = input()

lst1 = []
lst2 = []
flag = True

for mark in s:
    if mark == ')':
        flag = False
        lst1.pop()
        continue

    if flag:
        lst1.append(mark)

    else:
        lst2.append(mark)

if len(lst1) == len(lst2):
    print("correct")

else:
    print("fix")

