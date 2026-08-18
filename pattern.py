# for i in range(5):
#     print("*",end="") #horizontal printing

# for i in range(5):
#     print("*")         #vertical printing

# for i in range(1,6):    #pattern printing
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1,6,1):
#     print(i * "*")

# for i in range(6,0,-1):    #Reverse pattern printing
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(6,0,-1):
#     print(i * "*")


# for i in range(1,6):   #number pattern printing
#     for j in range(i):
#         print(j+1,end="")
#     print()


num=1
for i in range(1,6):   
    for j in range(i):
        print(num,end="")
        num+=1
    print()