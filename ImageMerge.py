from PIL import Image, ImageEnhance, ImageFilter
import os
from datetime import datetime

# import 2 img files
def merge(im1, im2):
    # cacl image size
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h)) # to save as .jpg change RGBA to RGB
    # write img 1
    im.paste(im1)
    # write img 2 where img 1 ends
    im.paste(im2, (im1.size[0], 0))

    return im
    
# set path to files    
path = 'C:\\Temp'
ext = ('.jpg', '.png')
#pathOut = 'C:\Temp\ImgOut'
# create blank image
mergedFile = Image.new("RGBA", (1, 1))
# name as date
currentDateTime = datetime.now().strftime("%d%m%Y%H%M%S")

for filename in os.listdir(path):
    if filename.endswith(ext):
        img = Image.open(f"{path}\{filename}")
        mergedFile = merge(mergedFile, img)
    else:
        continue
        
mergedFile.save(f"{path}\Merged_{currentDateTime}.png")
