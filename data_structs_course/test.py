def hash_string(s):
    return [ord(s[i])*(x**i) for i in range(len(s))]


    #return (sum([ord(s[i])*(x**i) for i in range(len(s)-1)]) % p) % m
    # (((119 + 111*263 + 114*(263**2) + 108*(263**3) + 100*(263**4)) % 1000000007) % 5)



global m
global p
global x
p = 1000000007
x = 263
m = 5

print(hash_string('world'))

print(119, 111*263, 114*(263**2), 108*(263**3), 100*(263**4))