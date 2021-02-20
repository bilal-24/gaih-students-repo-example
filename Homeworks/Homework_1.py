import random as rnd

matrix = []

for i in range(0,100):
    
    if i > 1:
        
        for j in range(2,i):
            
            if i % j == 0:
                break
        else:
            matrix.append(i)


#print(matrix)

row1 = [rnd.choice(matrix),rnd.choice(matrix),rnd.choice(matrix)]
row2 = [rnd.choice(matrix),rnd.choice(matrix),rnd.choice(matrix)]
row3 = [rnd.choice(matrix),rnd.choice(matrix),rnd.choice(matrix)]

print("\n",row1,"\n",row2,"\n",row3)
# thus, we can access the indexes as a matrix index



"""
print("\n",rnd.choice(matrix),rnd.choice(matrix),rnd.choice(matrix),"\n",
    rnd.choice(matrix),rnd.choice(matrix),rnd.choice(matrix),"\n",
    rnd.choice(matrix),rnd.choice(matrix),rnd.choice(matrix))
"""