s = {8, 7, 12, "Harry", [1,2]} # this will raise a type error


# here we cannot change the set elements cause they are immutable

# we can do this instead of list

s = {8, 7, 12, "Harry", (1,2)}

print(s)