def welcome():
    print("Hey ! Jitendra welcome")

print(__name__)
#if it is printing as __main__ then it is called from the jitendra.py
#and if it is printing as jitendra then it is called from some other python file
if __name__ == "__main__":
#this is used to print it only for the one time even if it is called for the import function and the jitendra.welcome is not commmented then also it will not be printed twice    
    welcome()    


#if_namemain.py is created for the creating the package and which is associated with this def welcome function
#reason of double printing is that it is printed once for the def welcome function and second time it is printed for import function