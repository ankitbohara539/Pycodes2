# This is how we find factorial of any number, using function in python
def Fact(n):
    if n == 1 or n == 0:
        return 1
    return n * Fact(n - 1)

while True:
    n = int(input("Enter a number: "))
    print(f"The factorial of {n} is: {Fact(n)}")

    choice = input("Do you want to ask another factorial? Yes/No ").strip().lower()
    if choice != "yes":
        print("Thank you for your time!")
        break

      

    

