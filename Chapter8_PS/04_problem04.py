
# sum = sum(n-1)

def sum_of_natural_num(n):
    if (n==1):
        return 1 
    return sum_of_natural_num(n-1)+n

print (sum_of_natural_num(9))

    

