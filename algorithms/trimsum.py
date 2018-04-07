def trimsum(n, csum):
    while True:
        if n == 0:
            return csum
            n, csum = n - 1, csum + n

print(trimsum(1000,0))
