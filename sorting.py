import os
import shutil
div = (__file__[:-10])
files = os.listdir(__file__[:-10])
if not ("jpg" in files) :
    os.system(f"md {div}\\jpg")
if not ("png" in files) :
    os.system(f"md {div}\\png")
if not ("gif" in files) :
    os.system(f"md {div}\\gif")
if not ("pdf" in files) :
    os.system(f"md {div}\\pdf")
    
for i in range(len(files)):
    if len(files[i]) >= 5 :
        print(str(files[i])[-3:])
        if str(files[i])[-3:] in ["png","jpg","gif","pdf"]:
            shutil.move(f"{div}{files[i]}", f"{div}{str(files[i])[-3:]}\\{files[i]}")