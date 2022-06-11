from collections import deque


def multi_check(num1, num2):
    if num2 % num1 == 0:
        return True
    return False


def solve():
    global num, ans
    if len(num) < 2:
         return

    cur = num.popleft()

    while True:
        if len(num) == 0:
            return
        nxt = num.popleft()
        if multi_check(cur, nxt):
            ans.append(nxt)
            break

    solve()

if __name__ == '__main__':
    num = deque()
    ans = []
    n = int(input())
    for _ in range(n):
        num.append(int(input()))

    solve()

    for elem in ans:
        print(elem)
