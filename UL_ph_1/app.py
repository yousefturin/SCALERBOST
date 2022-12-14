import os
from flask import Flask, flash, request, render_template, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from scaling import process_img


app = Flask(__name__, static_url_path='/static')

UPLOAD_FOLDER =  "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/input/" #reinput the correct full path !!!
CLIENT_IMAGES  = "C:/Users/youse/OneDrive/Documents/unviversity/4th Year/system programming/UL_ph_1/output"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

current_dateTime = datetime.now()
img_id = current_dateTime.microsecond


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["CLIENT_IMAGES"] = CLIENT_IMAGES 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.secret_key = "yusef-rayyan"




# checking if the file are under the allowed format
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def home():
        return render_template('index.html')


@app.route('/', methods = ['GET', 'POST'])
# creating the simple app that runs under the flask lib
def upload_image():
        global output_img
        if request.method == 'POST':
                file = request.files['file'] 
                width = request.form['width']
                height = request.form['height']
                asp = request.form.get('asp')
        # config for the image and input values "width"&"height"
                if 'file' not in request.files and 'width' not in request.form and 'height' not in request.form:
                        flash('No Image Part')
                        return redirect(request.url)
                if file.filename != ALLOWED_EXTENSIONS  and width == '' and height == '':
                        flash('Allowed image types are -> png, jpg, jpeg, gif')
                        return redirect(request.url)
                if file.filename == '' and width == '' and height == '':
                        flash('No Selected Image')
                        return redirect(request.url)
                if file.filename == '' and width != '' and height != '':
                        flash('No Selected Image')
                        return redirect(request.url)
                if file.filename == '' and width != '' and height == '':
                        flash('No Selected Image')
                        return redirect(request.url)
                if file.filename == '' and width == '' and height != '':
                        flash('No Selected Image')
                        return redirect(request.url)
                if file.filename != '' and width == '' and height == '':
                        flash('Please Input Width And Height')
                        return redirect(request.url)
                if file.filename != '' and width != '' and height == '':
                        flash('Please Input Height')
                        return redirect(request.url)
                if file.filename != '' and width == '' and height != '':
                        flash('Please Input Width')
                        return redirect(request.url)
                # checking if that file exist and allowed then pass it 
                if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                # convert the file name into a secure file by removing all the / from that name
                ext_filename = os.path.splitext(filename)
                # getting the fist part of the folder name
                prefix = ext_filename[0]
                # getting the second part of the folder name
                extension = ext_filename[1]
                # create f string with special name 
                filename_prefix_id_ext = f'{"Scalorbost_"}{str(datetime.now().strftime("%f"))}_{prefix}{extension}'
                # join the path with file name 
                root_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_prefix_id_ext) 
                # save the new filename
                save_path = os.path.join(root_path)
                file.save(save_path)
                output_img = process_img(save_path, width, height, filename_prefix_id_ext, asp)
                return redirect(url_for('download'))

                
        return render_template('index.html', filename = output_img )





#this is disable right now 
def page_not_found():
    return render_template('404.html'), 404


@app.route('/download')
def download():

    # render the 'download.html' template and pass the file name to the template
    return render_template('download.html', filename = output_img)


@app.route('/download/<filename>', methods=['GET', 'POST'])
def download_file(filename):
        try:
                print("this is file name>>>>>>>>>>>>>", filename)
                return send_from_directory(app.config['CLIENT_IMAGES'],
                        filename, as_attachment =True)
        except:
                page_not_found()
      

if __name__ =="__main__":
    app.run(debug= True)
# take the input of the image size as width and height to show the end user what is his image is then make some popup that the image hsd been uploaded!!!
