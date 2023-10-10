def are_files_equal(file1, file2):
    lines1 = open(r"C:\Learn JS\python use\files.txt", "r")
    lines1 = lines1.read()
    lines2 = open(r"C:\Learn JS\python use\files1.txt", "r")
    lines2 = lines2.read()

    if lines1 == lines2:
        print("True")
    else:
        print("False")


are_files_equal(r"C:\Learn JS\python use\files.txt", r"C:\Learn JS\python use\files.txt")
