def solve(y, x):
    global flag

    if col_visited[y] or row_visited[x] or dia1_visited[x+y] or dia2_visited[x-y+n-1]:
        flag = False
        return

    col_visited[y] = True
    row_visited[x] = True
    dia1_visited[x + y] = True
    dia2_visited[x - y + n - 1] = True


if __name__ == '__main__':
    n = 8
    flag = True
    cnt = 0

    chess = []
    dia1_visited = [False for _ in range(2*n)]
    dia2_visited = [False for _ in range(2*n)]
    col_visited = [False for _ in range(n+1)]
    row_visited = [False for _ in range(n+1)]

    for i in range(n):
        chess.append(list(map(str, input())))

    for row in range(n):
        for col in range(n):
            if chess[row][col] == '*':
                cnt += 1
                solve(row, col)

    if cnt != n or not flag:
        print("invalid")
    else:
        print("valid")
