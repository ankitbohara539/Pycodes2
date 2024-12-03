# here is program to change inch to cm

def inch_to_cm(inch):
    return inch*2.54

while True:
        n=int(input("Enter a value in inch:"))
        print(f"The corresponding value in CMS is:{inch_to_cm(n)}")

        choice = input("Do you want to check again ? Yes/No ").strip().lower()

        if choice != "yes":
            print("Thanks for using my function!")
            break
    
