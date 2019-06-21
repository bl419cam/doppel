from sklearn.base import BaseEstimator, TransformerMixin
import tensorflow as tf
import boto3
from PIL import Image
import numpy as np
from io import BytesIO
import requests

class ImageFeatureExtractor(BaseEstimator, TransformerMixin):
    """Extracts deep features from images."""
    
    
    def __init__(self, model="MobileNetV2", height=160, width=160):
        """Creates an ImageFeatureExtractor using the specified model."""
        self.height, self.width = height, width
        if model == "MobileNetV2":
            base_model = tf.keras.applications.MobileNetV2(
                input_shape=(height, width, 3),
               include_top=False,
               weights='imagenet'
            )
        else:
            raise Exception("Model unknown")
        global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
        self.model = tf.keras.Sequential([base_model, global_average_layer])
    
    def fit(self, X, y):
        """We're using a pre-trained model, so there's nothing to fit."""
        return self
    
    def transform(self, X):
        """Transforms image file paths into Numpy arrays of deep features."""
        result = []
        for image_pathname in X:
            result.append(self._transform_one(image_pathname))
        return result
    
    def _transform_one(self, image_pathname):
        """Transforms a single image pathname into deep features."""
        try:
            img = Image.open(image_pathname)
        except:
            response = requests.get(image_pathname)
            img = Image.open(BytesIO(response.content))
        img.load()
        img = img.convert("RGB") #add a third column for RGB to any arrays missing a 3rd
        image = np.asarray(img) 
        #print(image_pathname)   #show last working image
        image = image[:,:,:3]    #forces png images to be 3 colors
        return self._extract_features(image)
    
    def _prepare_image(self, image):
        """Converts an image to the expected format for prediction."""
        image = tf.cast(image, tf.float32)
        image = (image/127.5) - 1
        image = tf.image.resize(image, (self.height, self.width))
        return image
    
    def _extract_features(self, image):
        """Return a vector of 1280 deep features for image."""
        image_resized = self._prepare_image(image)
        image_np = image_resized.numpy()
        images_np = np.expand_dims(image_np, axis=0)
        image_np.shape, images_np.shape
        deep_features = self.model.predict(images_np)
        return deep_features[0]
    
    def fetch_image_from_s3(self, bucket, key):            
        """Fetches an image from S3 and returns a numpy array."""
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        body = response['Body']
        data = body.read()    
        f = BytesIO(data)
        image = Image.open(f)   
        image_data = np.asarray(image)
        return image_data
    
