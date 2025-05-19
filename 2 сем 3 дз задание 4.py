def prefix_to_string(prefix):
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
    return s