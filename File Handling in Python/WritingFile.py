# 1: Write()
File = open('TestFile.txt','w')
File.write("Hello World by Python Code ")
File.write("Author: Dhananjay")
File.close()
# 2: Using With : 
with open('TestFile.txt','w') as File:
    File.write("Hello World by Python Code ")
    File.write("Author: Dhananjay")
    print("Modification Completed.")
