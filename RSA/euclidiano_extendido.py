def euclidiano_extendido(a, b):
    x1, x2, x3 = 1, 0, 0
    y1, y2, y3 = 0, 1, 0
    
    while b != 0:
        q = a//b
        r = a%b

        x3 = x1 - q * x2
        y3 = y1 - q * y2

        a = b
        b = r

        x1, y1 = x2, y2
        x2, y2 = x3, y3
    return y1
