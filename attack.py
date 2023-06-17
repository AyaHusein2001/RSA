import math
import Assign as RSA
def prime_factorization(n):
    # Find the smallest prime factor of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # i is a prime factor of n
            p = i
            break
    
    # Find the other prime factor of n
    q = n // p
    
    return p, q

def attack(ciphers,n,e,plain):
    p, q = prime_factorization(n)
    fin=(p-1)*(q-1)
    d=int(pow(e,-1,fin))
    m=''
    for cipher in ciphers:
        m+=RSA.rsa_decrypt(n,d,cipher)
    v=RSA.verify(m,plain)
    return m,v

def write_to_file(file_name, x):
    # Open the file for writing
    with open(file_name, "a") as file:
        
        file.write(str(x)+"\n")

