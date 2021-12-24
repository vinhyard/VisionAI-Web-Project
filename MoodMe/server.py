
from flask import Flask, render_template, request, redirect, url_for
import age_gender
import os
import config
import face_exp2
app = Flask(__name__)

#save images to static/images folder
app.config['IMAGE_UPLOADS'] = f'static/Images'

#importing images with greater security.
#prevent hacking/phishing
from werkzeug.utils import secure_filename



@app.route('/img/<filename>/<age>/<gender>/<mood>')
def img(filename,age, gender, mood):

    return render_template("img.html",filename=filename ,age=age, gender=gender, mood=mood)
@app.route('/main',methods=['POST', "GET"])
def upload_image():
    if request.method == "POST":
        print(request.files)
        #capture file name
        print('test0')
        image = request.files['file-upload-field']
        print(image)
        print('test4')
        #if file has no name
        if image.filename == '':
            print("File name is invalid")
            
            return redirect(request.url)
        print('test3')
        filename = secure_filename(image.filename)
        print("test1")
        #access directory of folder to upload our file.
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir, app.config['IMAGE_UPLOADS'], filename))
        print("test2")
        #predict mood
        mood = face_exp2.face_exp(f'static/Images/{filename}')
        mood[0].upper()
        print(mood)
        age, gender = age_gender.read_img(f'static/Images/{filename}')
        print(age, gender)
        return redirect(url_for('img', filename=filename, age=age, gender=gender, mood=mood))
    return render_template("main.html")


#route to display the image
@app.route('/display/<filename>')
def display_image(filename):
    
    return redirect(url_for('static', filename='/Images/'+filename), code=301) #code=301 for security





app.run(port=5000)
