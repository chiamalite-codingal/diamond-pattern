rowsize = int(input("Enter rows:"))
if rowsize % 2 == 0:  #even condition
    halfdiamrow = int(rowsize/2)
else:
    halfdiamrow = int(rowsize/2)+1
space = halfdiamrow -1
#upper part
for i in range(1,halfdiamrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space = space -1
    num = 1
    for j in range(2*i-1):
        print(end=str(num)+" ")
        num = num + 1
    print("\n")