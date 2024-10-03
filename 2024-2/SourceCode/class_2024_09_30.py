def dec2bin(n):
    # n = 17 
    # str_b = '10001'

    if n <= 1:
        return [n]
    else:
        new_n = n//2
        resto = n%2
        return dec2bin(new_n) + [resto] 
    
if __name__ == '__main__':

    print(dec2bin(16))
    print(dec2bin(17))
    print(dec2bin(15))
    print(dec2bin(1))
    print(dec2bin(0))
    print(dec2bin(2))
    print(dec2bin(5))