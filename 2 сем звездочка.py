def z_to_prefix(z):
    n = len(z)
    s = [0] * n
    s[0] = 'a'
    c = ord('b')

    for i in range(1, n):
        if z[i] > 0:
            for j in range(i, i + z[i]):
                if j < n and s[j] == 0:
                    s[j] = s[j - i]
        if s[i] == 0:
            s[i] = chr(c)
            c += 1
    prefix = [0] * n

    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    return prefix


print(z_to_prefix([0, 0, 1, 0, 3, 0, 1]))


def prefix_to_z(prefix):
    n = len(prefix)
    s = [0] * n
    s[0] = 'a'
    c = ord('b')

    for i in range(1, n):
        if prefix[i] > 0:
            s[i] = s[prefix[i] - 1]
        else:
            s[i] = chr(c)
            c += 1
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


print(prefix_to_z([0, 0, 1, 0, 1, 2, 3]))
