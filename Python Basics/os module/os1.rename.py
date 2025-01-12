import os

for i in range(0,25):
    os.rename(f"Books/category{i+1}",f"Books/type{i+1}")
    #here first f string is used for the source and second is for the destination. The os.rename() function is used to rename the file or directory. The source is the current name of the file or directory
    print(f"Renamed category {i+1} to type {i+1}")