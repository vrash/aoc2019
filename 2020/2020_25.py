#dh, rank 372
a = 1614360
b = 7734663
mod = 20201227
c = 0
val = 1
while val != a:
    val = (7 * val) % mod
    c += 1
print(pow(b,c,mod))
