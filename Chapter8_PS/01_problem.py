a = int(input("Enter number for a: "))
b = int(input("Enter number for b: "))
c = int(input("Enter number for c: "))

def greatest_num(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
print(f" The biggest number is : {greatest_num(a,b,c)} ")