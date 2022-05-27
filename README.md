# Image-Metadata-Remover-Script
Removes metadata AKA (EXIF) information on all images detected (except .gif files)

This script will remove metadata from the images found on the passed path including its subfolders.

* Since the script corrupts animated .gif files, those files are ignored by the script.
* __WARNING:__ Source files are replaced with the metadata-removed version.

# The Script:

```python


import os
import sys
from PIL import Image

def remove_data(image_path: str) -> bool:
        if not os.path.exists(image_path):
            print(f"'{image_path}' Doesn't exist!")
            return False
        try:
            if image_path.endswith('.gif'):
                return[]
            else:
                image = Image.open(image_path)
                image_data = list(image.getdata())
                new_image = Image.new(image.mode, image.size)
                new_image.putdata(image_data)
                new_image.save(image_path)
            if os.path.isfile((os.path.dirname(image_path)) + '\\' + 'folder.jpg'):
                pass
            else:
                new_filename = ((os.path.dirname(image_path)) + '\\' + 'folder.jpg')
                os.rename(image_path, new_filename)
                return True
        except Exception as err:
            print(err)
            return False
            
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

def dothis():
    count = 0
    loop = 0
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            count += 1
    for filename in os.listdir(directory):
        remove_data(directory + '\\' + filename)
        loop += 1
        print("Removed exif data for " + str(loop) + '/'+ str(count) +' files in ' + directory)

source_input = str(input("Please paste the directory containing images: "))
source_dir = (source_input)
source_dir = source_dir.strip('"')
source_dir2 = source_dir.replace('[', 'o[o')
source_dir2 = source_dir2.replace(']', 'o]o')
source_dir2 = source_dir2.replace('o[o', '[[]')
source_dir2 = source_dir2.replace('o]o', '[]]')
directory = source_dir2.replace('#', '[#]')
folderssub = fast_scandir(directory)

for directory in folderssub:
    dothis()

else:
    dothis()

```
