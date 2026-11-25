def x(a, b, c, n):
    t = a + b + c

    if t >= 70:
        g = "A"
    elif t >= 60:
        g = "B"
    elif t >= 50:
        g = "C"
    else:
        g = "F"

    print(n, t, g)
    return t
