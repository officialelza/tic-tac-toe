s= 'Hello World'
print(s[::-1])

import hashlib

s = 'Aleena123elxa2233'

encoded = hashlib.sha256(s.encode()).hexdigest()

print(encoded)
print("-"*60)



def resets():
    ...
tupl1 = tuple(1,2,3,45)
print(*tupl1)
