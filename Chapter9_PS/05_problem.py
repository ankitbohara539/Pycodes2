# This is a program to wheather a item in word with txt file replace its lenth with # symbol

word = ['Jawan','PATHAN','Donkey', 'Movie']

with open ("file.txt",'r') as f:
    content = f.read()

for words in word:
    content = content.replace(words, '#' * len(words))


    with open ("file.txt",'w') as f:
        f.write(content)
