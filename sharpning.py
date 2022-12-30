from PIL import Image, ImageEnhance, ImageFilter
import os

REDIRECT_FOLDER =  "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/output/"
PROCESS_FOLDER = "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/process/"
SAVE_FOLDER = ""


def img_sharp(save_path, filename_prefix_id_ext, sharpness_factor):
    new_sharpness_factor = float(sharpness_factor)
    SAVE_FOLDER = save_path
    # Open the image
    img = Image.open(SAVE_FOLDER)
    # Calculate the new width and height for a DPI of 300
    new_width = img.width *2.125
    new_height = img.height *2.125
    # Cast the new width and height to integers
    new_width = int(new_width)
    new_height = int(new_height)
    resized_im = img.resize(( new_width,new_height), resample=Image.BICUBIC)
    # Create an ImageEnhance object for sharpening
    enhancer = ImageEnhance.Sharpness(resized_im)
    # Apply the sharpening effect
    sharpened_im = enhancer.enhance(new_sharpness_factor )
    sharpened_im = sharpened_im.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=3))
    # Apply median filtering to the sharpened image
    filtered_im = sharpened_im.filter(ImageFilter.MedianFilter(size=3))
    # Save the filtered image
    output_img = filtered_im.save(filename_prefix_id_ext)
    ext_img = os.path.split(filename_prefix_id_ext)
     # getting the fist part of the folder name
    prefix = ext_img[0]
    # getting the second part of the folder name
    extension = ext_img[1]
    # create f string with special name 
    img_prefix_id_ext = f'{"Scalorbost"}_{prefix}_{new_width}_{new_height}_{"Image_Enhancing_by"}_{sharpness_factor}_{extension}'
    # join the path with file name 
    output_img = os.path.join(REDIRECT_FOLDER, img_prefix_id_ext) 
    os.rename(filename_prefix_id_ext, output_img)
    #>>>EVERYTHING IS WORKING PERFECTLY 
    return img_prefix_id_ext

