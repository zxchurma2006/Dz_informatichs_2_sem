def cycles(s, text):
    n = len(s)
    S = s + s
    p = S + '*' + text
    m = len(p)
    z = [0] * m
    l, r = 0, 0

    for i in range(1, m):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < m and p[z[i]] == p[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    k = 0

    for i in range(n, len(z)):
        if z[i] >= n:
            k += 1
    return k

print(cycles("abc", "abcabc"))
