with open ("log.txt") as f :
    content = f.read() 

with open ("renamed_by_py.txt","w") as f: 
 f.write(content)