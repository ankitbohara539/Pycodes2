# Here we've a Program to change tempreture fahrenheit to celsius
def f_to_c(f):
    return 5*(f-32)/9 # Formulae for F to C
f = int(input("Enter tempreture in Fahrenheit:"))
c = f_to_c(f)
print (f"{round(c,2)} Celsius") # round is function used to round a number to a specified number of decimal places.
 
