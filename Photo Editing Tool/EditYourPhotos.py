from PIL import Image, ImageEnhance, ImageFilter
import os

path = "/Users/gersonmolina/Desktop/Python Authomation Projects/Image Editor Automation Program/imgs"

pathOut = "/Users/gersonmolina/Desktop/Python Authomation Projects/Image Editor Automation Program/editedImgs"

    #Acess all of the images in the folder and applies all the code below to it
for fileName in os.listdir(path):

    #The variable img, holds the image(object. Which will allow us to do some edits to it by calling it
    img = Image.open(f"{path}/{fileName}")

    edit = img.filter(ImageFilter.SHARPEN)

    contrast = 1.5
    enhancer = ImageEnhance.Contrast(edit)

    edit = enhancer.enhance(contrast)

    cleanName = os.path.splitext(fileName)[0]

    edited = edit.save(f'{pathOut}/{fileName}')

print(edited)