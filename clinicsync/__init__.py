from flask import Flask

import tensorflow as tf
# import keras

from keras.applications.imagenet_utils import decode_predictions
from keras.models import model_from_json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np

# You can use pretrained model from Keras
# Check https://keras.io/applications/
# load json and create model
json_file = open('clinicsync/models/pnemonia_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("clinicsync/models/pnemonia_model.h5")
print("Loaded model from disk")

print('Model loaded. Check http://0.0.0.0:5002/')


# Model saved with Keras model.save()
#MODEL_PATH = 'models/your_model.h5'

# Load your own trained model
# model = load_model(MODEL_PATH)
model._make_predict_function()          # Necessary
print('Model loaded. Start serving...')


def model_predict(img, model):
    img = img.convert('RGB')
    img = img.resize((226, 226))

    # Preprocessing the image
    x = np.array(img)
    print(x.shape)

    #x = np.true_divide(x, 255)
    #x = preprocess_input(x, mode='tf')
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)

    return preds

app = Flask(__name__)

import clinicsync.views
