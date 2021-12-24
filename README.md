# VisionAI-Web-Project

<div id="top"></div>


<h3 align="center">VisionAI-Web-Project</h3>

  <p align="center">
    This project uses open-sourced neural networks to create a trait profit for an individual in a photo. 
  
 



<!-- ABOUT THE PROJECT -->
## About The Project
This project was built to test my abilties in the visionai/web specialties. This program allows a user to upload an image and recieve a profile card that contains
the predicted age, mood, and gender of the individual in the photo.

  
##Mistakes made
At first; I trained a deeplearn model using numpy and shape (48, 1, 1), however when I tested photos on the program I could not reshape the image to (48, 48). This was costly in time and if I had looked for multiple different options in the beginning, I could have saved a few hours in time. 
  
##Improvements
React could be used to improve the layout of the front end. Implement a back/again button. If this project was a public website, using concurrency and parallel programming would increase processing speed. Adding more functions such as ethnicity detection, face-mask detection, etc.
 
##Conclusion
I enjoyed this experience and learned a lot more about visionAI and web design. 
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

*Flask(https://flask.palletsprojects.com/en/2.0.x/)
*TensorFlow(https://www.tensorflow.org/)
*Opencv(https://opencv.org/)
*deepFace(https://github.com/serengil/deepface)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
1.) start virtualenv
2.) pip install -r requirements.txt
3.) git clone https://github.com/misbah4064/age_and_gender_detection.git
4.) pip install gdown
5.) cd age_gender_detection
6.) gdown https://drive.google.com/uc?id=1_aDScOvBeBLCn_iv0oxSO8X1ySQpSbIS
7.) unzip modelNweight.zip
8.) enter 'export FLASK_APP=server.py'
9.) enter 'flask run'
10.) '127.0.0.1:5000/main' in browser to reach main page




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
        * Predict age
        * Predict mood
        * Predict gender
        * Generate profile card


<p align="right">(<a href="#top">back to top</a>)</p>







<p align="right">(<a href="#top">back to top</a>)</p>



