### Bradley Assaly-Nesrallah
### bassalyn@uwo.ca
### 250779140
### Written Oct 23, 2020
### 
### Usage: solve(N,e,d)

##Implementation of fast powering algorithm
##input:base, power and modulo p integers
##output base^power mod p integer

from generate_input import generate_input

def rapidExponentiation( base, power, p ):

    result = 1                              #start with 1
    while power != 0:                     # loop until power = 0
        if power % 2 == 1:                #odd pow -1 exp
            result = (result * base) % p
        power = power // 2                  # ^power = ^power/2
        base = (base * base) % p            # base = base * base

    return result

##implementation of exteded euclidean algorithm go compute gcd
##input integers a and b
##output gcd of the integers a and b
def eeagcd(a, b):
    x,y, u,v = 0,1, 1,0             ##base case
    while a != 0:                   ##while a not 0 loop
        q, r = b//a, b%a            ##EEA implenetation from textbook
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd                      ##eturns gcd




# Based on math proof of part 1
# Input : (N,e,d) N=pq primes, e an encryption exponent, d a decryption exponent in RSA
# Output: Returns either p or q in a tuple (p,q) or (q,p) or fails
def solve(N, e, d):
    m=2                         ##set variables
    k=0
    f=e*d-1                ##computes ed-1modN
    while(f%2==0):              ##finds k and r dividing f by 2 repeatedly
        f=f//2
        k=k+1
    r=f
    if 2//N:                    ##checks if 2|N for completeness
        return 2,N//2
    while (m<N):                ##for each m value loops
        u=0                     ##sets u=0 and increments m
        m = m + 1
        if m//N:                ##if m//N then returns p=m,q=N/m
            p=m
            q=N//m
            return p,q
        g= eeagcd(rapidExponentiation(m,r,N)-1,N) ##computes gcd(m^r-1,N)
        if g!=1 and g!=N:         ##if gcd!=1 or N then returns p=g,q=N/g
                p=g
                q=N//g
                if p<q:
                    return p,q
                else:
                    return q,p
        while u!=k:             ##loops through different exponents u<k
                                ##computes gcd(m^(2u)r-1,N)
            g = eeagcd(rapidExponentiation(m,((2**u)*r)%N,N)+1,N)
            if g!=1 and g!=N:     ##if gcd!=1 or N then returns p=g,q=N/g
                p = g
                q = N // g
                if p < q:
                    return p, q
                else:
                    return q, p
            u=u+1               ##increment u

##function to verify that e*dmodphi(pq)=1
##returns True if so, false otherwise
def check(N,e,d):
    p=solve(N,e,d)[0]
    q=solve(N,e,d)[1]
    phi=(p-1)*(q-1)        ##returns bool true if check holds otherwise false
    if(d*e)%phi==1:
        return True
    return False

##main function, solves for all tuples obtained from generate input.py
if __name__ == "__main__":
    input_tuples = generate_input("912")
    for tuple in input_tuples:          ##solves and outputs for each tuple
        print(
            'solve({0}, {1}, {2})'.format(tuple[0], tuple[1], tuple[2]),
            solve(tuple[0], tuple[1], tuple[2]),
            check(tuple[0], tuple[1], tuple[2]),
            sep='\n\t\t=',
            end='\n\n'
        )


