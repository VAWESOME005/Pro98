def swapFiles():
    file1 = input("Enter the First File You Want to Swap: ")
    file2 = input("Enter the Second File You Want to Swap: ")
    file1Open = open(file1)
    file2Open = open(file2)
    file1Read = file1Open.read()
    file2Read = file2Open.read()
    file1Open = open(file1, 'w')
    file2Open = open(file2, 'w')
    file1Open.write(file2Read)
    file2Open.write(file1Read)
    print("Files Swapped!")
    

swapFiles()