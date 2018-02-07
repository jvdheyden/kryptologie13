import sys
import math

P_KEY = (613,989)

def rsa(x):
    e = P_KEY[0]
    n = P_KEY[1]

    return (x ** e) % n

def primesUpTo(n):
    primes = [2]
    i = 3
    while (i <= n):
        prime = True
        for j in primes:
            if (i % j == 0):
                prime = False
                break
        if (prime == True):
            primes.append(i)
        i += 2
    return primes

def factorize(n):
    primes = primesUpTo(n)
    for i in primes:
        for j in primes:
            if ((i*j) == n):
                return (i,j)

def decrypt(y):
    e = P_KEY[0]
    n = P_KEY[1]
    (p,q) = factorize(n)
    phi = (p-1)*(q-1)
    d = _egcd(e, phi)
    return y**d % n

def differenceOfSquares(n):
    a = math.ceil(math.sqrt(n))
    b = 0
    while ((a * b) < n):
        a += 1
        b = math.sqrt(a**2 - n)
        if (b.is_integer() and ((a+b)*(a-b) == n)):
            return (int(a+b), int(a-b))

def _egcd(x,n):
    r0 = n
    r1 = x
    r2 = n % x
    q = n // x
    s_2 = 1
    t_2 = -1 * q
    #print('{} =  {} * {} + {}'.format(r0,q,r1,r2))
    #print('{} = {} * r0 + {} * r1 '.format(r2,s_2,t_2))
    r0 = r1
    r1 = r2
    q = r0 // r1
    r2 = r0 % r1
    s_1 = (-1) * q * s_2
    t_1 = 1 - (q * t_2)
    #print('{} =  {} * {} + {}'.format(r0,q,r1,r2))
    #print('{} = {} * r0 + {} * r1 '.format(r2,s_1,t_1))
    while(r2 != 1):
        r0 = r1
        r1 = r2
        q = r0 // r1
        r2 = r0 % r1
        t = t_2 - (t_1 * q)
        s = s_2 - (q * s_1)
        t_2 = t_1
        s_2 = s_1
        #print('{} =  {} * {} + {}'.format(r0,q,r1,r2))
        #print('{} = {} * r0 + {} * r1 '.format(r2,s,t))
        t_1 = t
        s_1 = s
    if (r2 != 1):
        print('gcd(x,n) != 1')
    else:
        return t % n

print rsa(444)
print factorize(989)
print decrypt(444)
print differenceOfSquares(989)
print differenceOfSquares(9382619383)
print differenceOfSquares(4386607)
