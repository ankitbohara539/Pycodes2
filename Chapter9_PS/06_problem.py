with open ('log.txt','r') as f:
   content = f.read()

if ("python" in content):
   print(" This string is on content")

else:
   print(" This string is not on content")
   
   