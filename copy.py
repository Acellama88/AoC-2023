import shutil, os
choice = input("Which day should I create? ")
os.mkdir(f"Day {choice}")
shutil.copy("temp.py",f".//Day {choice}//Day{choice}_p1.py")
shutil.copy("temp.py",f".//Day {choice}//Day{choice}_p2.py")