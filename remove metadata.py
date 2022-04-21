

import os
import sys
from PIL import Image

def remove_data(image_path: str) -> bool:
        if not os.path.exists(image_path):
            print(f"'{image_path}' Doesn't exist!")
            return False
        try:
            image = Image.open(image_path)
            image_data = list(image.getdata())
            if image_path.endswith('.gif'):
                return[]
            else:   
                new_image = Image.new(image.mode, image.size)
                new_image.putdata(image_data)
                new_image.save(image_path)  
            return True
        except Exception as err:
            print(err)
            return False
            
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

def meme():
    count = 0
    loop = 0
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            count += 1
    for filename in os.listdir(directory):
        remove_data(directory + '\\' + filename)
        loop += 1
        print("Removed exif data for " + str(loop) + '/'+ str(count) +' files in ' + directory)
    
directory = str(input("Please paste the directory containing images: "))
folderssub = fast_scandir(directory)
#if fast_scandir(directory):
    #response = input("Subfolders found, would you like to run the script on these folders too? (y/n): ")
    #if response == 'y':
        #meme()
for directory in folderssub:
    meme()
#else:
    #meme()
else:
    meme()

