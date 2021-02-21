list1 = []
list2 = []
def prime_first(n):
    
    for j in range(2, n):
        if n % j == 0:
            return None
    else:
        return n
        


def prime_second(n):
    
    for k in range(2, n):
        if n % k == 0:            
            return None
    else:
        return n


for i in range(1, 1000):
    
    if i == 1:
        continue

    elif i < 500:       
        if prime_first(i) != None:
            prime_first(i)
            list1.append(i)
    
    else:
        if prime_second(i) != None:
            prime_second(i)
            list2.append(i)
print("First Prime:",list1)
print("\nSecond Prime:",list2)

