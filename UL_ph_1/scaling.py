
import os
from PIL import Image
REDIRECT_FOLDER =  "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/output/"
PROCESS_FOLDER = "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/process/"
SAVE_FOLDER = ""


def process_img(save_path, width, height, filename_prefix_id_ext, asp):
    # Cast the new width and height to integers
    target_width = int(width)
    target_height = int(height)
    SAVE_FOLDER = save_path
    img = Image.open(SAVE_FOLDER)
    img_width, img_height = img.size
    # Calculate the scaling factor for the target width
    scaling_factor_width = target_width / img_width

    # Calculate the scaling factor for the target height
    scaling_factor_height = target_height / img_height

    # Choose the smallest scaling factor
    scaling_factor = min(scaling_factor_width, scaling_factor_height)

    # Calculate the new width and height of the image
    new_width = int(img_width* scaling_factor)
    new_height = int(img_height * scaling_factor)
    if asp:

        img = img.resize((new_width, new_height), resample=Image.BICUBIC)

    else:
        img = img.resize((new_width, new_height),resample=Image.BICUBIC )

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

