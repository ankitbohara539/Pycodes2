for i in range (1,6):
    print(i)


# This is code to generate table from 1 to 20

  # Printing multiplication tables from 1 to 20
for num in range(1, 21):  # Loop through numbers 1 to 20
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):  # Loop through 1 to 10 for each table
        print(f"{num} x {i} = {num * i}")
    print("-" * 20)  # Separator between tables
