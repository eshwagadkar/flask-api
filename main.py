from flask import Flask, jsonify, request
from flask_cors import CORS
from torch.functional import split
from model_files.ml_predict import predict_plant, Network
from pyfcm import FCMNotification
import base64
from decouple import config

app = Flask("Plant Disease Detector")
CORS(app)
push_service = FCMNotification(api_key=config('API_KEY'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)