import os
# Creating A File 
def create(filename):
    with open(filename,'w') as File:
        File.write("Hello Bhupendra Jogi")
        print("File Created")
    
# Renaming a File
def rename(filename, newFileName):
        os.rename(filename,newFileName)
        print("File Renamed")
# Deleting a File
def delete(filename):
    os.remove(filename)
    print("File Deleted")

#Call the Functions Here:
    create('Demo1.txt')
    