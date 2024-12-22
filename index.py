#Question one Row pattern
num = int(input("Enter row number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        
        print("*",end=" ")
    print()    

# odd number in column in * pattern function
num = int(input("Enter your Row: "))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()   

#  Even number in column in * pattern function
num = int(input("Enter your Row: "))
k=2
for i in range(0,num+1):
    for j in range(1,k+1):
        print(j,end=" ")
    k=k+2

    print()  

# question print pyramid * in row
num = int(input("Enter your Row: "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print() 
# 
# # Question print Reverse pyramid * in row
num = int(input("Enter your Row: "))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")   
    print()     