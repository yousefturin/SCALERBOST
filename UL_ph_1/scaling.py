import cv2
import os
REDIRECT_FOLDER =  "C:/Users/ENVY/Documents/unviversity/4th Year/system programming/UL_ph_1/output/"
SAVE_PATH =  "C:/Users/ENVY/Documents/unviversity/4th Year/system programming/UL_ph_1/input/Scalorbost_834088_Untitled-1.png"
width = 1024
height = 1024

def process_img():

    img = cv2.imread(SAVE_PATH)
    global width, height
    width = width
    height = height 
    dimention = (width, height) 
    resized_img = cv2.resize(img, dimention)
    new_path_img = cv2.imwrite(os.path.join(REDIRECT_FOLDER , 'waka.jpg'), resized_img)# this is new
    ext_img = os.path.splitext(new_path_img)
    # getting the fist part of the folder name
    prefix = ext_img[0]
    print(prefix)
    # getting the second part of the folder name
    extension = ext_img[1]
    print(extension)
    # create f string with special name 
    img_prefix_id_ext = f'{"Scalorbost_"}_{width}_{height}_{prefix}{extension}'
    print(img_prefix_id_ext)
    # join the path with file name 
    root_path = os.path.join(REDIRECT_FOLDER, img_prefix_id_ext) 
    print(root_path)
    # save the new filename
    save_path = os.path.join(root_path)
    print(save_path)
    output_img = os.save(save_path)# need to fix this one no output img is saved so the code is not doing anything 


    return output_img

if __name__ == "__main__":
    process_img()