word = "JAWAN"
with open ("file.txt",'r') as f:
    content = f.read()

    contentNew = content.replace(word, "PATHAN")


    with open ("file.txt",'w') as f:
        f.write(contentNew)
