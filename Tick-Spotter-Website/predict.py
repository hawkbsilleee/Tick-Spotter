from skimage import transform 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import keras

MODEL_PATH = 'weights/5-25-23_BasicCNN_50epochs'
# '/Volumes/My Passport/weights/5-25-23_BasicCNN_50epochs'
# 'weights/5-25-23_BasicCNN_50epochs' 
#'/Volumes/My Passport/weights/5-24-23_BasicCNNTest'
model = keras.models.load_model(MODEL_PATH)

def load(filename):
    """Loads image as np array from filename"""
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (256,256,3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image

def predictor(image):
    """
    Run model on numpy image array to generate prediction
    Returns: a tuple (species name: str, confidence: str)
    """
    image_load = load(image)
    # result is a 4 item list nested in a list 
    result = model.predict(image_load) 
    # access the nested list 
    result = result[0]

    # map each value in the results list to a species class confidence  
    preds = {
        "Amblyomma Americanum": result[0], 
        "Dermacentor Variabilis": result[1],
        "Ixodes Scapularis": result[2],
        "Non-tick": result[3]
    }

    # select the item in preds that has the highest confidence 
    prediction = max(preds, key=preds.get)
    return (prediction, str(preds[prediction]*100) + '%')

