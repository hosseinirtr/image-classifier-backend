from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2

# Load the model once when the module is imported
model = InceptionResNetV2(weights='imagenet')