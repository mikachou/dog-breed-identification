import json
import sys
import tensorflow as tf
from huggingface_hub import hf_hub_download

tf_model = hf_hub_download(repo_id='mikachou/dog-breed-classifier', filename='tf_model.h5')
config_json = hf_hub_download(repo_id='mikachou/dog-breed-classifier', filename='config.json')

model = tf.keras.models.load_model(tf_model)
print(model.summary())

with open(config_json) as f:
    config = json.load(f)

dogs_breeds = list(config['id2label'].values())

# see https://towardsdatascience.com/convert-images-to-tensors-in-pytorch-and-tensorflow-f0ab01383a03
img = tf.io.read_file(sys.argv[1])
tensor = tf.io.decode_image(img, channels=3, dtype=tf.dtypes.float32)
tensor = tf.image.resize(tensor, [299, 299])
input_tensor = tf.expand_dims(tensor, axis=0)

print(tf.shape(input_tensor))

output = model.predict(input_tensor)
high_score = max(output[0])

predicted_breed = dogs_breeds[list(output[0]).index(high_score)]

print(predicted_breed, '| score =', high_score)