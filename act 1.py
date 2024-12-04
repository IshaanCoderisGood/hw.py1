n = int(input("Enter number: "))
c = m = 0

while n:
    if n & 1:
        c += 1
        if c > m: m = c
    else: c = 0
    n >>= 1

print(m)
