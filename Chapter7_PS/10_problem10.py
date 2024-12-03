# int(input('Enter a number:'))
n = 5               
for i in range(1, n+1): # for loop it iterates through each row of the square

    if (i==1 or i==n):  # this is condition, checks wheather current row is first or the last, if true, it prints (n) asteris like boundry square
        print("*"*n, end = "")
    else:
        print("*", end="")
        print(" "*(n-2),end="")
        print("*",end="")

    print("")