
from flask import Flask, render_template, request, redirect

import os
import face_expression
import config
app = Flask(__name__)

#save images to static/images folder
app.config['IMAGE_UPLOADS'] = f'{config.directory}/static/Images'

#importing images with greater security.
#prevent hacking/phishing
from werkzeug.utils import secure_filename




@app.route('/main',methods=['POST', "GET"])
def upload_image():
    if request.method == "POST":
        print(request.files)
        #capture file name
        image = request.files['file']
        
        #if file has no name
        if image.filename == '':
            print("File name is invalid")
            
            return redirect(request.url)
            
        filename = secure_filename(image.filename)
        
        #access directory of folder to upload our file.
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir, app.config['IMAGE_UPLOADS'], filename))

        #predict mood
        mood = face_expression.predict_mood(f'{config.directory}/static/Images/{filename}')
        if mood == "happy"

        age, gender = age_gender.read_img(f'{config.directory}/static/Images/{filename}')
        return render_template("img.html", filename=filename, mood=mood, age=age, gender=gender)
    return render_template("main.html")



#route to display the image
@app.route('/display/<filename>')
def display_image(filename):
    
    return redirect(url_for('static', filename='/Images/'+filename), code=301) #code=301 for security





app.run(port=5000)
