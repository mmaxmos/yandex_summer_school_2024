N = int(input())
K = int(input())
m = list(map(int, input().split()))
f = 0
l = 0.5
for i in range(K, N):
    c = 0
    if m[i] != l:
        for j in range(0, i):
            if m[i] > m[j]:
                c += 1
    if (c / i) >= 0.9:
        f = 1
        print(i+1)
        break
    l = m[i]
if f == 0:
    print(-1)



# Выводим результат
print(result)