a = int(input("Enter the Limit"))
for i in range(a):
    for j in range(i):
        print(" ", end=" ")    
    for j in range(a-i):
        print("*", end=" ")
    print()