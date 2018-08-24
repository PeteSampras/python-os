import os
#1. Open the filenames.txt file with read-only access with the open() function
my_file=open('filenames.txt','r')
#2. Print the name of the file and if it is open or closed using the .name and .closed properties
print(f'File {my_file.name} is closed: {my_file.closed}')
#3. Use a for loop to read all lines of filenames.txt into a list variable
my_list = []
for line in my_file:
    my_list.append(line)
#4. Print out all the lines from the file from your variable
for each in my_list:
    print(each)
#5. Close the filenames.txt file and print if the file is open or closed
my_file.close()
#6. Create a file using the open() function called secrets.txt
new_file=open('secrets.txt','w')
#7. Write your own secrets to the file with the write() function
for i in range(0,4):
    new_file.write(f'secret{i}\n')
#8. Close the secrets.txt file using the close() method. DON'T FORGET!
new_file.close()
#9. Print out the contents of the text file in your terminal to prove it worked
new_file=open('secrets.txt','r') 
for line in new_file:
    print(line)
new_file.close()
#10. Open your secrets.txt file in append mode and write some more super secret info
new_file=open('secrets.txt','a') 
for i in range(5,9):
    new_file.write(f'secret{i}\n')

#11. Close the secrets.txt file again using the close() function
new_file.close()
#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function
os.rename('secrets.txt','.supersecret.txt')
#13. See if you can see the file in your file explorer

#14. Create a list variable named file_names that contains a list of filenames
file_names=[]
#15. Use the writelines() function to append the filenames to the filenames.txt file
with os.scandir() as it:
    for each in it:
        file_names.append(it)
#16. Delete the initial secrets.txt file now that you have a super secret hidden version
#os.remove('secrets.txt')
#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.
this=input("Please input file name to create.")
that=open(this,'w')
that.close()