import os

f=[]
for _, _, filenames in os.walk("C:/User/dir/path/copy"):
    f.extend(filenames)

print(len(f))
