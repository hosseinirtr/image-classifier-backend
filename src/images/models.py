from base64 import decode
from distutils.command.upload import upload
from django.db import models
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from tensorflow.keras.applications.inception_resnet_v2 import decode_predictions, preprocess_input
import time
import os
import shutil
from .model_loader import model  # Import the preloaded model

def refresh_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


class Image(models.Model):
    picture = models.ImageField()
    classified = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classified at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the image first

        # Add a delay of a few seconds
        time.sleep(5)

        try: 
            print(f"{self.picture.path} , 10 seconds wait over")
            img = load_img(self.picture.path, target_size=(299, 299))
            img_array = img_to_array(img)
            to_pred = np.expand_dims(img_array, axis=0)
            prep = preprocess_input(to_pred)

            # Use the preloaded model to predict
            prediction = model.predict(prep)
            decoded = decode_predictions(prediction)[0][0][1]
            self.classified = str(decoded)
            print(decoded)
            print('success in process')

            # Save the changes to the `classified` field
            super(Image, self).save(update_fields=['classified'])
        except FileNotFoundError as ex:
            print('File or directory not found: ', ex)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
