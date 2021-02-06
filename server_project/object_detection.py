import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np


class IdentifyObjects:
    '''
    Tf-Hublink -  https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1
    '''

    def __init__(self):
        # self.detector = hub.load("https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1")
        self.detector = hub.KerasLayer("hub/openimages_v4_ssd_mobilenet_v2_1")

    def predict(self, image_path):
        im = Image.open(image_path)
        image_arr = np.array(im)
        converted_img = tf.image.convert_image_dtype(image_arr, tf.float32)[tf.newaxis, ...]
        det_out = self.detector(converted_img)
        class_ids = det_out["detection_class_labels"]
        return class_ids
