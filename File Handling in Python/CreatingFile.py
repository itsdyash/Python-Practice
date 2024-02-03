import os
def create(filename):
    with open(filename,'w') as File:
        File.write("Hello Bhupendra Jogi")
        print("File Created")
# Reading a File
def read(filename):
    with open(filename,'r') as File:
        Data = File.read()
        print(Data)
# Appending a File 
def append(filename):
    with open(filename,'a') as File:
        File.write(" US Mein Kaha gaye ho?")
        print("File Appended")
    
# Renaming a File
def rename(filename, newFileName):
        os.rename(filename,newFileName)
        print("File Renamed")
# Deleting a File
def delete(filename):
    os.remove(filename)
    print("File Deleted")

#Call the Functions Here:
    