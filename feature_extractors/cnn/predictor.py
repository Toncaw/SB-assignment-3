import cv2, sys
import numpy as np
import tensorflow as tf
from tensorflow.keras import models

class CNN:
    def __init__(self, resize=100, model='model_opt2.h5'):
        self.resize = resize
        self.model = models.load_model(model)

    def predict(self, img):
        img_arr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        new_arr = cv2.resize(img_arr, (self.resize, self.resize))

        X_predict = np.array(new_arr).reshape(-1, self.resize, self.resize, 1)
        X_predict = X_predict/255.0

        prediction = self.model.predict(X_predict)
        predictionBest = prediction[0]

        best_class = np.argmax(predictionBest)

        return predictionBest, best_class

if __name__ == '__main__':
    cnn_predictor = CNN()