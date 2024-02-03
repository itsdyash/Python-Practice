# There is 3 ways to read a file in python.
# 1: for Loop
File = open('TestFile.txt','r')
for i in File:
    print(i)
    
# 2: read
File = open('TestFile.txt','r')
print(File.read())
    
# 3: Using  with statement (Recommended way)
with open('TestFile.txt','r') as File:
    File = File.read()
    File = File.split()
    print(File)