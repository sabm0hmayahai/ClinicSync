from flask import url_for, request, render_template, Response, jsonify, redirect
from clinicsync import app,model_predict,model
import numpy as np
from clinicsync.util import base64_to_pil
from datetime import datetime

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Save the image to ./uploads
        # img.save("./uploads/image.png")

        # Make prediction
        preds = model_predict(img, model)

        pred_class = preds.argmax(axis=-1)
        print(pred_class)
        if(pred_class == [0]):
            pred_class = "NORMAL"
        else:
            pred_class = "PNUEMONIA"
        # Process your result for human
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        #pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        result = str(pred_class)               # Convert to string
        result = result.replace('_', ' ').capitalize()

        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)
    return None


@app.route('/pneumonia')
def pneumonia():
    # make this an API endpoint
    print("API endpoint reached")

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home',year=datetime.now().year)


@app.route('/disease2')
def disease2():
    # make this an API endpoint
    print("reached second disease")