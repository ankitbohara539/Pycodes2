
def word_remove(list, word):
    n = []
    for item in list:
        if word not in item :
            n.append(item)
        else:
            n.append(item.replace(word,""))
    return n
    
list = [ "Ankit","Anjali","Anita","Yesha","Nepal"]
print (word_remove(list, "An"))
        





