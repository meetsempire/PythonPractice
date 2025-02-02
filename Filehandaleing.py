file=open("exp.txt", "w")
a=input("Enter the text:")

file.write(a+'\n')

file.close()

file1=open("exp.txt", "r")
for each in file1:
   print(each)


with open("exp.txt") as firstfile, open("exp2.txt", "a") as secondfile:
   for line in firstfile:
       secondfile.write(line)
       
       
file2= open("exp2.txt",'a')
file2.write("Everything is well, weather is clwaer today")
file2.close()


file3=open("exp2.txt", "r")
for each in file3:
   print(each)
