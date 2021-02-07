#!/usr/bin/env python
import keras
from PIL import Image, ImageOps
import numpy as np

def fashion_image_classification(img, weights_file):
    
    # Load the model
    model = keras.models.load_model(weights_file)

    # Create an array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img

    # Image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the array
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into an array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    return np.argmax(prediction)
    # Return the prediction with the highest probability






