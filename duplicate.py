from os import walk
import shutil

path = "C:/User/dir/path"
path_to = "C:/User/dir/path/copy"
f = ['uy']

for _, _, filenames in walk(path):
    for fa in filenames:
        with open(path + fa, 'r') as txt_file:
           text = txt_file.readlines()
        
        if f:
            if not text in f:
                f.append(text)
                shutil.copy(path + fa, path_to)

print('files copied in a new directory without duplacate content')