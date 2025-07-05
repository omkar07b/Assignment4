try:
    file1 = open("sample.txt","r")

    print("Reading file content:\n")
    line1 = file1.readline()
    line2 = file1.readline()
    print("Line 1:",line1)
    print("Line 2:",line2)
    file1.close()
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found.")