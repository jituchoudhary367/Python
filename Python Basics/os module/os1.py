import os

if(not os.path.exists("Books")):
    os.mkdir("Books")
    
for i in range(0,25):
    os.mkdir(f"Books/category{i+1}")
    