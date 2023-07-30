# Flask app for TickSpotter

Basic website that enables a user to upload an image file of a potential tick to a trained CNN that
outputs a prediction on the species of tick of the image. 

## Python Files:
### app.py 
Back end that runs the app
### predict.py
Runs trained model on image provided through app.py

## HTML Files (all located in the templates folder)
### base.html 
Template that all html pages inherit from 
### index.html 
home page 
### about.html 
about page 
### navbar.html 
nav bar, other pages inherit
### upload.html 
upload form
### reults.html 
results page generated after form is uploaded   

## Static Files (located in static folder)
### css/main.css 
CSS styling for all html pages 
### imgs/.. 
logo images 
### js/main.js 
currently not used 
