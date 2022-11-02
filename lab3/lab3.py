print("\t\t\t\t\tPyramid of Numbers")

for i in range(1 , 11):
    for j in range(11-i):
        print(" ", end = " ")
    for j in range (1, i):
        print (j, end = " ")
    for i in range(i, 0, -1 ):
        print(i, end = " ")

print("\n") 