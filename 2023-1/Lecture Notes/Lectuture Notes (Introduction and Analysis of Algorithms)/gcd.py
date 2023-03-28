def gcd(a, b):
    while b != 0:
        t = b
        b = a mod b
        a = t
    return a