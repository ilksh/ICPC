n = int(input())
ans = []

for _ in range(n):
    keyword = "Simon says"
    s = input()
    if keyword in s:
        new_s = s[len(keyword):]
        print(new_s)
