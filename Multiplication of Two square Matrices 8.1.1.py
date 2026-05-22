n = int(input("dimension: "))

print("first matrix:")
a = [list(map(int, input().split())) for _ in range(n)]

print("second matrix:")
b = [list(map(int, input().split())) for _ in range(n)]

c = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]

print("Resultant Matrix:")

for i in range(n):
    print(*c[i])
