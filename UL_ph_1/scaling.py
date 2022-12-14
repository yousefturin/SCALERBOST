import cv2
import os
from PIL import Image
REDIRECT_FOLDER =  "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/output/"
PROCESS_FOLDER = "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/process/"
SAVE_FOLDER = ""


def process_img(save_path, width, height, filename_prefix_id_ext, asp):
    int_width = int(width)
    int_height = int(height)
    SAVE_FOLDER = save_path
    img = Image.open(SAVE_FOLDER)

    if asp:
        img.thumbnail((int_width, int_height))

    else:
        img = img.resize((int_width, int_height))

    output_img = img.save(filename_prefix_id_ext)
    ext_img = os.path.split(filename_prefix_id_ext)
    # getting the fist part of the folder name
    prefix = ext_img[0]
    # getting the second part of the folder name
    extension = ext_img[1]
    # create f string with special name 
    img_prefix_id_ext = f'{"Scalorbost"}_{prefix}_{width}_{height}_{"ASPECT_RATIO_is"}_{asp}_{extension}'
    # join the path with file name 
    output_img = os.path.join(REDIRECT_FOLDER, img_prefix_id_ext) 
    os.rename(filename_prefix_id_ext, output_img)
    #>>>EVERYTHING IS WORKING PERFECTLY 
    return img_prefix_id_ext

