import os
from flask import Flask, flash, request, render_template, redirect, url_for,send_from_directory ,abort, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
from scaling import process_img
from sharpning import img_sharp

app = Flask(__name__, static_url_path='/static')


UPLOAD_FOLDER =  "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/input/" #reinput the correct full path !!!
CLIENT_IMAGES  = "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/output"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

current_dateTime = datetime.now()
img_id = current_dateTime.microsecond


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["CLIENT_IMAGES"] = CLIENT_IMAGES 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.secret_key = "teqi-Eest1-iold4"

class ResourceNotFoundError(Exception):
    pass

class InternalServerError(Exception):
    pass



@app.errorhandler(ResourceNotFoundError)
def handle_resource_not_found(e):
    return render_template('error.html', error=e), 404

@app.errorhandler(InternalServerError)
def handle_internal_server_error(e):
    return render_template('error.html', error=e), 500



@app.route('/')
def home():
        try:
                return render_template('main.html')
        except:
                raise ResourceNotFoundError("Resource page not found")
                

@app.route('/rescale')
def rescale():
        try:
                return render_template('index.html')
        except:
                raise ResourceNotFoundError("Resource page not found")
@app.route('/enhance')
def enhance():
        try:
                return render_template('enhance.html')
        except:
                raise ResourceNotFoundError("Resource page not found")



def fetching_rescale(file, filename, width, height, asp):
        global output_img #>>it a bad idea 
      

        try:
                # convert the file name into a secure file by removing all the / from that name
                ext_filename = os.path.splitext(filename)

        except:

                raise InternalServerError("Internal server could not return Image Split")  

        try:
                # getting the fist part of the folder name
                prefix = ext_filename[0]
                # getting the second part of the folder name
                extension = ext_filename[1]
        except:

                raise InternalServerError("Internal server could not return Image Prefix") 

        try:
                # create f string with special name 
                filename_prefix_id_ext = f'{"Scalorbost_"}{str(datetime.now().strftime("%f"))}_{prefix}{extension}'
        except:

                raise InternalServerError("Internal server could not return Image Rename")    

        try:
                # join the path with file name 
                root_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_prefix_id_ext) 
        except:

                raise InternalServerError("Internal server could not return Image Join Path") 

        try:
                # save the new filename
                save_path = os.path.join(root_path)
                file.save(save_path)
        except:
                raise InternalServerError("Internal server could not return Image Save")  

        try:
                output_img = process_img(save_path, width, height, filename_prefix_id_ext, asp)
                return download()
        except:
                raise ResourceNotFoundError("Image Resource could not be retuned in rescaling")


# checking if the file are under the allowed format
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/rescale', methods = ['GET', 'POST'])
def upload_image():
        
        if request.method == 'POST':
                file = request.files['file'] 
                width = request.form['width']
                height = request.form['height']
                asp = request.form.get('asp')
                
        # config for the image and input values "width"&"height"
                if 'file' not in request.files and 'width' not in request.form and 'height' not in request.form:
                        flash('No Image Part')
                        return redirect(request.url)
                else:
                        if (file.filename == '' and width != '' and height != '') or (file.filename != '' and width == '' and height == ''):
                                flash('No Selected Image, Input Width And Height')
                                return redirect(request.url)
                                
                        elif (file.filename == '' and width == '' and height == ''):
                                flash('No Selected Image, Input Width And Height')
                                return redirect(request.url)

                        elif (file.filename == '' and width != '' and height == '') or (file.filename != '' and width != '' and height == ''):
                                flash('No Selected Image, No Height Selected')
                                return redirect(request.url)
                        
                        elif (file.filename == '' and width == '' and height != '') or (file.filename != '' and width == '' and height != ''):
                                flash('No Selected Image, No Width Selected')
                                return redirect(request.url)

                        # checking if that file exist and allowed then pass it 
                        if file and allowed_file(file.filename):
                                try:
                                        filename = secure_filename(file.filename)
                                        return fetching_rescale(file, filename, width, height, asp) 
                                except:
                                        raise ResourceNotFoundError("Image Resource could not be processed in rescaling")   

                        elif file.filename not in ALLOWED_EXTENSIONS :
                                flash('Allowed image types are \n (png, jpg, jpeg, gif)')
                                return redirect(request.url)
                        
                        else:
                                raise ResourceNotFoundError("Image Resource could not be retuned in rescaling")  
        else:
                return render_template('index.html')




def fetching_sharp(file, filename, sharpness_factor):
        global output_img #>>it a bad idea 
      

        try:
                # convert the file name into a secure file by removing all the / from that name
                ext_filename = os.path.splitext(filename)

        except:
                raise InternalServerError("Internal server could not return Image Split")

        try:
                # getting the fist part of the folder name
                prefix = ext_filename[0]
                # getting the second part of the folder name
                extension = ext_filename[1]
        except:
                raise InternalServerError("Internal server could not return Image Prefix") 
                

        try:
                # create f string with special name 
                filename_prefix_id_ext = f'{"Scalorbost_"}{str(datetime.now().strftime("%f"))}_{prefix}{extension}'
        except:
                raise InternalServerError("Internal server could not return Image Rename")  

        try:
                # join the path with file name 
                root_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_prefix_id_ext) 
        except:
                raise InternalServerError("Internal server could not return Image Join Path")                          

        try:
                # save the new filename
                save_path = os.path.join(root_path)
                file.save(save_path)
        except:
                raise InternalServerError("Internal server could not return Image Save") 
        try:
                output_img = img_sharp(save_path, filename_prefix_id_ext, sharpness_factor)
                return download()
        except:
                raise ResourceNotFoundError("Image Resource could not be retuned in enhancing")



@app.route('/enhance', methods = ['GET', 'POST'])
def sharp_img():
        if request.method == 'POST':
                file = request.files['file'] 
                sharpness_factor = request.form['sharpness_factor']
                if 'file' not in request.files and 'sharpness_factor' not in request.form:
                        flash('No Image Part')
                        return redirect(request.url)
                else:
                        if file and allowed_file(file.filename):
                                try:
                                        filename = secure_filename(file.filename)
                                        return fetching_sharp(file, filename, sharpness_factor) 
                                except:
                                        raise ResourceNotFoundError("Image Resource could not be processed in enhancing")
                        elif file.filename not in ALLOWED_EXTENSIONS :
                                flash('Allowed image types are \n (png, jpg, jpeg, gif)')
                                return redirect(request.url)
                        else:
                                raise ResourceNotFoundError("Image Resource not found in File")

        else:
                return render_template('enhance.html')
                        
                




@app.route('/download')
def download():
        try:
    # render the 'download.html' template and pass the file name to the template
                return render_template('download.html', filename = output_img)
        except:
                raise ResourceNotFoundError("Resource page not found")
                

@app.route('/download/<filename>/', methods=['GET'])
def download_file(filename):
        try:
                return send_from_directory(app.config['CLIENT_IMAGES'],
                        filename, as_attachment =True)
        except:
                raise ResourceNotFoundError("Image Resource not found")
      



if __name__ =="__main__":
    app.run(debug= True)

