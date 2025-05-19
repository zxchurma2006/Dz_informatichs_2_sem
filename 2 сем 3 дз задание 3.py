def z_to_string(z):
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
    return s