a = input("Enter text to write to the file:")

file1 = open("output.txt","w")
writing_file = file1.write(a)
print("Data successfully written to output.txt.\n")
file1.close()

b = input("Enter additional text to append:")
file1 = open("output.txt","a")
appending_file = file1.write(b)
print("Data successfully appended.\n")
file1.close()

file1 = open("output.txt","r")
print("Final content of output.txt:")
Final = file1.read()
print(Final)
file1.close()