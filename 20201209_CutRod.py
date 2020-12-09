#  20201209

# Bottom-up
def CutRod(table, n):
    r = [0] * (n+1)
    for i in range(1, n + 1):
        if n == 0:
            return 0
        q = 0
        for j in range(1, n + 1):
            q = max(q, table[min(j, len(table) - 1)] + r[i - j])
            print(r)
            r[i] = q
    return r[n] #, r
table = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
x = int(input("How long is your rod? "))
print("-"*30+"\nMax Value:", CutRod(table, x), ".")
