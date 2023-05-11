# What is SCALERBOST
It's a web application written in Python using the Flask framework and it allows users to upload an image to the server and then apply either a scaling or sharpening process to the image, In scaling process users must select a desired width and height for the image to be either down scale or upscale based on the image itself and the user input of width and height and for enhance images users must select a desired sharpness factor .
![Screenshot 2023-05-11 135255](https://github.com/yousefturin/SCALERBOST/assets/94796673/7328874d-4f10-4edc-9a73-e6206e804f69)
# Install Dependency
```
./python dependency.py
```
# Configuration
For SCALING or ENHANCING images the allowded formats are ["png", "jpg", "jpeg", "gif"], the maximum size that can be uploaded to the sever is 16 MB as an image, for the dimensions, width maximum is 3840px and height is 2160px.

*To run this web application you need to change **UPLOADED_FOLDER** and **CLIENT_IMAGES** path to your path in **app.py**. 

```
UPLOAD_FOLDER =  "C:/Users/name/your/path/to/this/directory/UL_ph_1/input/"
```

```
CLIENT_IMAGES =  "C:/Users/name/your/path/to/this/directory/UL_ph_1/output/"
```
Then change the **REDIRECT_FOLDER** and **PROCESS_FOLDER** path to your path in **scaling.py** and **sharpning.py**.
```
REDIRECT_FOLDER =  "C:/Users/name/your/path/to/this/directory/UL_ph_1/output/"
```
```
PROCESS_FOLDER = "C:/Users/name/your/path/to/this/directory/UL_ph_1/process/"
```
## SCALING

This process takes the uploaded image by user and read the width and height of the image then it calculate the scaling factory for the desired width and height,

After that to keep the aspect ratio function it select the smalest factor between width and height, then uses the .resize function form pillow to resize the image either to upscale or dwonscale then stores the image under a new name with ID in the output file /output and send it back to the user to the download.html page.
![Screenshot 2023-05-11 135351](https://github.com/yousefturin/SCALERBOST/assets/94796673/efffe4b8-d992-4556-916d-b4387d0cfd6b)
## ENHANCING
This process takes the uploaded image by user and calculate the width and height for a DPI of 300 then cast the width and heith to integers then it resize the image using the .resize fucntion form pillow library then it creates an ImageEnhance object for sharpening and apply a sharpening effect to the resized image using enhance function and then apply a filer UnsharpMask with radius=2  percent=200 threshold=3.

After that it apply a 3x3 medianFilter then stores the image under a new name with ID in the output file /output and send it back to the user to the download.html page.
![result_2](https://github.com/yousefturin/SCALERBOST/assets/94796673/6fe036d3-65ed-46d7-8d2b-7263cfe3e752)
![result_3](https://github.com/yousefturin/SCALERBOST/assets/94796673/6a7c7ce9-cc2b-41e9-b8a5-075070c7a7a0)
