f = open ('bio.txt')

check = f.read()

if ( "person" in check):
    print("The word person in the document")

else:
    print("The word person not in the document")


f.close()

