# Face-Mask Detection
---
**Team Masquerade**:mask: <br/>:heavy_check_mark: Wear a mask and be safe!! 
---
"If I'am not personally at high risk for COVID-19, why should I wear a mask?"If this type of attitude goes on... we won't be able to fight against Novel Corona Virus.<br/>
India has been unlocking in phases. Malls, temples and other public places has been unlocked. Things are back to normal but, it is not "new normal". Wearing masks is must but still many people resist to do so.

# Overview

Now-a-days, entering any public premises is dangerous, with more possibilites of spreading of COVID-19. With respect to this problem, here comes our proposed system! The COVID-19 Face-Mask Detector. It is a real-time operating system, which detects if a person enetring the premises is wearing mask or not. If yes, its says, "Great! You have got your mask on! Kindly use sanitizer, have a great day!":thumbsup: and if you're not, "Kindly wear your mask! You are not allowed to enter!":thumbsdown:. <br/>The model we've build could be potentially used to ensure the saftey.

# Desciption
This is a real-time image classification project trained on the top of Keras/Tensorflow API with MobileNetV2. The model <a href="https://github.com/SheCodes-IEEE-CIS-GHRCE/Face-Mask-Detection/blob/main/TRAINING.ipynb"> TRAINING.ipynb</a> is trained with two datasets(link at the bottom) consiting of images with people weaing masks and people not wearing masks. Thus we obtained <a href="https://github.com/SheCodes-IEEE-CIS-GHRCE/Face-Mask-Detection/blob/main/mask_detection.h5"> mask_detection.h5 </a>, trained model. To run the detector, run <a href="https://github.com/SheCodes-IEEE-CIS-GHRCE/Face-Mask-Detection/blob/main/detector.py"> detector.py. </a> Detector starts, click on the start button to start detection, enter time to terminate the detector and then detection will go on. At the end of the day, system will generate a pie chart showing how many people enetrin the premises were wearing maks and who were not. Piechart is stored in your local systems which can be used for future analysis.</br> Follow the <a href="https://drive.google.com/drive/folders/1xYgh4S8fPZMW2Q-umZ_6_MjenBrSWEKO?usp=sharing">GUIDELINES</a> to run the detector.</br>Here is a demonstration by one of our teammate,
<a href="https://drive.google.com/file/d/1Iro2nYpVpV3_M1ukq9m6mI9yr-4h4uay/view?usp=drivesdk"> DEMONSTRATION:woman_technologist: </a>
<br></br>

### PROCESS FLOW 
<img src="https://github.com/SheCodes-IEEE-CIS-GHRCE/Face-Mask-Detection/blob/main/PROCESS%20FLOW.jpeg">
<br></br>

# Modules/ Packages required
* numpy: Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
* matplotlib: Matplotlib is an amazing library for data visualization. It comes with a wide variety of plots. Plots helps to understand trends, patterns, and to make correlations.
* tensorflow: Is a Python-friendly open source library for numerical computation that makes machine learning faster and easier.
* OpenCV: It is an open source Computer Vision and Machine Learning software library, used to develop real-time CV applications.
* gTTS: It is used to convert entered text into audio which can later be saved as mp3 file.
* os: It helps to interact with Operating System.
* sys: This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
* SpeechRecognition: library used for speech recognition.
* playsound: Module used to play audio files.
* tkinter: Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. 
<
# Technologies Used
![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://keras.io/img/logo.png" width=200>](https://keras.io/) 

[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=170>](https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png)

[<img target="_blank" src="https://www.gstatic.com/devrel-devsite/prod/vbf66214f2f7feed2e5d8db155bab9ace53c57c494418a1473b23972413e0f3ac/tensorflow/images/lockup.svg" width=280>](https://www.gstatic.com/devrel-devsite/prod/vbf66214f2f7feed2e5d8db155bab9ace53c57c494418a1473b23972413e0f3ac/tensorflow/images/lockup.svg)




# :two_women_holding_hands:Team Members:two_women_holding_hands:
* <a href="https://github.com/aditibodade">Aditi Bodade</a>
* <a href="https://github.com/Sonali2824">Sonali Preetha Nandagopalan</a>
* <a href="https://github.com/Mitaliii">Mitali Sahu</a>
* <a href="https://github.com/NoorpreetKaur">Noorpreet Kaur</a>


## DATASET LINK:
<a href="https://drive.google.com/drive/folders/1XDte2DL2Mf_hw4NsmGst7QtYoU7sMBVG"> 📂 DATASET LINK </a>
<br></br>
