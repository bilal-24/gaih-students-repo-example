

def prime_first(n):
    
    for j in range(2, n):
        if n % j == 0:
            return None
    else:
        return n, "in First Prime Numbers"  


def prime_second(n):
    
    for k in range(2, n):
        if n % k == 0:            
            return None
    else:
        return n, "in Second Prime Numbers"


for i in range(1, 1000):
    
    if i == 1:
        continue

    elif i < 500:       
        if prime_first(i) != None:
            print(prime_first(i))
    
    else:
        if prime_second(i) != None:
            print(prime_second(i))

