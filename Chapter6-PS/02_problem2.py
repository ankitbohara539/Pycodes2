
marks1 = int(input("Enter marks you achive1:"))
marks2 = int(input("Enter marks you achive2:"))
marks3 = int(input("Enter marks you achive3:"))

total = (100*(marks1 + marks2 + marks3 ))/300   # this is total percentage

if (total>=40 and marks1>=33 and marks2>=33 and marks3>= 33):

    print("Congratulation you're pass", total)
else:
    print("you're failed, try next year",total)

print(" END")