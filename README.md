# VisionAI-Web-Project

<div id="top"></div>


<h3 align="center">VisionAI-Web-Project</h3>

  <p align="center">
    This project uses open-sourced neural networks to create a trait profit for an individual in a photo. 
  
 



<!-- ABOUT THE PROJECT -->
## About The Project
This project was built to test my abilties in the visionai/web specialties. This program allows a user to upload an image and recieve a profile card that contains
the predicted age, mood, and gender of the individual in the photo.

 <p>
   
<h2>Mistakes made</h2>
At first; I trained a deeplearn model using numpy and shape (48, 1, 1), however when I tested photos on the program I could not reshape the image to (48, 48). This was costly in time and if I looked for multiple different options in the beginning, I could have saved a few hours in time. My Mac was also unable to utilize some of the DeepLearn models. The dataset used to train the models at first were not accurate, and had a val-accuracy of about 56%. 
 </p>
 <p>
<h2>Improvements</h2>
React could be used to improve the layout of the front end. Implement a back/again button. If this project was a public website, using concurrency and parallel programming would increase processing speed. Adding more functions such as ethnicity detection, face-mask detection, celebrity look-alike, etc. would further enhance the experience. 
 </p>
 <p>
<h2>Conclusion</h2>
I enjoyed this experience and learned a lot more about visionAI and web design. The debugging process took the most time. This is because I had experience in building Flask/Django projects, which made it easier to understand how to connect the front/backend. 
</p>


<h1>Built With</h1>
<ul>
  <li>Flask(https://flask.palletsprojects.com/en/2.0.x/)</li>
  <li>TensorFlow(https://www.tensorflow.org/)</li>
  <li>Opencv(https://opencv.org/)</li>
  <li>deepFace(https://github.com/serengil/deepface)</li>
</ul>




<!-- GETTING STARTED -->
<h1>Getting Started<h1>
  <ol>
    <li>start virtualenv</li>
    <li>pip install -r requirements.txt</li>
    <li>git clone https://github.com/misbah4064/age_and_gender_detection.git</li>
    <li>pip install gdown</li>
    <li>cd age_gender_detection</li>
    <li>gdown https://drive.google.com/uc?id=1_aDScOvBeBLCn_iv0oxSO8X1ySQpSbIS</li>
    <li>unzip modelNweight.zip</li>
    <li>enter 'export FLASK_APP=server.py'</li>
    <li>enter 'flask run'</li>
    <li>'127.0.0.1:5000/main' in browser to reach main page</li>
  </ol>




<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
1.) Upload a photo into the main page.
![Screen_Shot_2021-12-24_at_2 15 27_PM](https://user-images.githubusercontent.com/83558837/147373803-74657a03-c437-489d-80c0-b70f973848af.png)

2.) Recieve profile card of photo that includes age, mood, and gender.
![Screen_Shot_2021-12-24_at_4 20 06_PM](https://user-images.githubusercontent.com/83558837/147373797-b8bb23ca-4308-44d0-837f-e1558b20f63d.png)
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

Features:
        <ul>
  <li>Predict age</li>
  <li>Predict mood</li>
  <li>Predict gender</li>
  <li>Generate profile card</li>
        </ul>









