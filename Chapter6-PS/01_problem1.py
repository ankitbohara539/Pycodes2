a1 = int(input("Enter a number a1:"))
a2 = int(input("Enter a number a2:"))
a3 = int(input("Enter a number a3:"))
a4 = int(input("Enter a number a4:"))

if (a1>a2 and a1>a3 and a1>a4):
    print("The gretest number is a1:",a1)
elif (a2>a1 and a2>a3 and a2>a4):
    print("The gretest number is a2:",a2)
elif (a3>a1 and a3>a2 and a3>a4):
    print("The gretest number is a3:",a3)
# if (a1>a2 and a1>a3 and a1>a4):
#     print("The gretest number is a1",a1)

else:
    print("a4 is greatest:",a4)

    