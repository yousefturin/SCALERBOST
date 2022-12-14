from PIL import Image
path = 'C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/input/Scalorbost_066102_wallpaper-1266599.png'
image = Image.open(path)
print(image)

sunset_resized = image.resize((400, 400))
sunset_resized.save('sunset_400.png')
