from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'C:\Temp'
pathOut = 'C:\Temp\Edited'

for filename in os.listdir(path):
    # load image:
    img = Image.open(f"{path}/{filename}")

    # edit:
    edit = img.filter(ImageFilter.SHARPEN)
    
    factor = 1.2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    

    # save:
    cleanName = os.path.splitext(filename)[0]
    # os.path.splitext() split the path name to root and ext [0]C:\Temp\file [1].jpg
    edit.save(f"{pathOut}/{cleanName}_edited.png")
