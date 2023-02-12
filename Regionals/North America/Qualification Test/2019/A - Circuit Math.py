alphabet = {}
for i in range(65, 91):
    character = chr(i)
    alphabet[character] = False

n = int(input())
value = list(map(str, input().split()))
for i in range(n):
    num = i+65
    if value[i] == 'T':
        alphabet[chr(num)] = True

command = list(map(str, input().split()))
logic = ['*', '+', '-']
stack = []
for elem in command:
    if elem in logic:
        if elem != '-':
            a = stack.pop()
            b = stack.pop()

            if elem == '*':
                stack.append(a and b)
            elif elem == '+':
                stack.append(a or b)
        else:
            cur = stack.pop()
            stack.append(not cur)
    else:
        stack.append(alphabet[elem])

if stack[0]:
    print('T')
else:
    print('F')