# Hate-Speech-Detection

- [Problem Statement](#problem-statement)
- [Libraries Used](#libraries-used)
- [Approach](#approach)
- [Setup](#setup)
- [Contributors](#contributors)


> Hate Speech detection using Machine Learning

## Problem Statement

Hate Speech are a set of prohibited words/actions because they can that trigger violent attitude/acts towards other individuals or groups. So in this project we detect whether a given sentence involves hate speech. We have also deployed the model Using Flask on Heroku.<br>

Check out the project at https://hate-speech-detectionn.herokuapp.com/

## Libraries Used

- pandas
- numpy
- matplotlib
- sklearn 
- Flask

## Approach

The Jupyter [notebook](https://github.com/hot9cups/Hate-Speech-Detection/blob/main/hate_speech_detection.ipynb) contains three methods that can be used for classification - 
- Count-vectoriser(Naive approach)
- TF-IDF features(Improvement)
- RNN(Best performance)

In the deployed app, the model uses ridge classification(essentially ridge regression but using a threshold to turn it into a classifier) which is a simple linear model.<br>
This isn't ideal for such a task, and shall be changed to use RNNs like is done in the notebook.

## Setup

1) Clone the repository to your local machine<br>
``` git clone https://github.com/hot9cups/Hate-Speech-Detection.git ```

2) cd to the root of cloned repo and Run app.py<br>
``` python app.py```

3) Visit localhost:8000 (You can alternatively directly visit [this](https://hate-speech-detectionn.herokuapp.com/) link) to see the application running. Here is the screenshot of the app in action : <br>
<img src="https://github.com/shubham5351/Hate-Speech-Detection/blob/main/Screenshots/1.JPG" width=1000 height=600></img>

4) Enter the text which you want to classify : <br>
<img src="https://github.com/shubham5351/Hate-Speech-Detection/blob/main/Screenshots/2.JPG" width=1000 height=600></img>

5) Classification of the review : <br>
<img src="https://github.com/shubham5351/Hate-Speech-Detection/blob/main/Screenshots/3.JPG" width=1000 height=600></img>

## Contributors

- [Ayush Modi](https://github.com/hot9cups) - ML Modeling & Analysis Part
- [Shubham Pawar](https://github.com/shubham5351) - Frontend & Deployment Part
