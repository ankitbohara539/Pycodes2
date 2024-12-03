
def multiplication_table(n):
    for i in range (1,11):
        print(f"{n}X{i}={n*i}")  

while True:
    n = int(input("Enter a number:"))
    multiplication_table(n)
    choice = input("Do you want next nums table ? yes/no").strip().lower()
    
    if choice != "yes":
        print("Dhanyabad Sir 🙏")
        break

        