import tensorflow as tf
import numpy as np
from flask import Flask, request
from PIL import Image
import io

# Load the saved CNN model
model = tf.keras.models.load_model(r'E:\NOTTS\Year 3\Final Year Project\Spring\Foodopedia\Jupyter\TFMobileVNet2.model')

# Define a Flask app
app = Flask(__name__)

# Define an API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    image = request.files['image'].read()
    
    # Preprocess the image--------------
    # Open the image using PIL
    image = Image.open(io.BytesIO(image))

    # Resize the image to 224x224
    image = image.resize((224, 224))

    # Convert the image to a numpy array
    image = np.array(image)

    # Expand the dimensions of the image to match the expected shape of the model input
    image = np.expand_dims(image, axis=0)
    
    # Pass the preprocessed image to the CNN model
    proba = model.predict(image)
    
    # Get the predicted class index
    class_index = np.argmax(proba)
    
    # Convert the class index to the class name
    class_names = {
    0: 'apple_pie',
    1: 'baby_back_ribs',
    2: 'baklava',
    3: 'beef_carpaccio',
    4: 'beef_tartare',
    5: 'beet_salad',
    6: 'beignets',
    7: 'bibimbap',
    8: 'bread_pudding',
    9: 'breakfast_burrito',
    10: 'bruschetta',
    11: 'caesar_salad',
    12: 'cannoli',
    13: 'caprese_salad',
    14: 'carrot_cake',
    15: 'ceviche',
    16: 'cheesecake',
    17: 'cheese_plate',
    18: 'chicken_curry',
    19: 'chicken_quesadilla',
    20: 'chicken_wings',
    21: 'chocolate_cake',
    22: 'chocolate_mousse',
    23: 'churros',
    24: 'clam_chowder',
    25: 'club_sandwich',
    26: 'crab_cakes',
    27: 'creme_brulee',
    28: 'croque_madame',
    29: 'cup_cakes',
    30: 'deviled_eggs',
    31: 'donuts',
    32: 'dumplings',
    33: 'edamame',
    34: 'eggs_benedict',
    35: 'escargots',
    36: 'falafel',
    37: 'filet_mignon',
    38: 'fish_and_chips',
    39: 'foie_gras',
    40: 'french_fries',
    41: 'french_onion_soup',
    42: 'french_toast',
    43: 'fried_calamari',
    44: 'fried_rice',
    45: 'frozen_yogurt',
    46: 'garlic_bread',
    47: 'gnocchi',
    48: 'greek_salad',
    49: 'grilled_cheese_sandwich',
    50: 'grilled_salmon',
    51: 'guacamole',
    52: 'gyoza',
    53: 'hamburger',
    54: 'hot_and_sour_soup',
    55: 'hot_dog',
    56: 'huevos_rancheros',
    57: 'hummus',
    58: 'ice_cream',
    59: 'lasagna',
    60: 'lobster_bisque',
    61: 'lobster_roll_sandwich',
    62: 'macaroni_and_cheese',
    63: 'macarons',
    64: 'miso_soup',
    65: 'mussels',
    66: 'nachos',
    67: 'omelette',
    68: 'onion_rings',
    69: 'oysters',
    70: 'pad_thai',
    71: 'paella',
    72: 'pancakes',
    73: 'panna_cotta',
    74: 'peking_duck',
    75: 'pho',
    76: 'pizza',
    77: 'pork_chop',
    78: 'poutine',
    79: 'prime_rib',
    80: 'pulled_pork_sandwich',
    81: 'ramen',
    82: 'ravioli',
    83: 'red_velvet_cake',
    84: 'risotto',
    85: 'samosa',
    86: 'sashimi',
    87: 'scallops',
    88: 'seaweed_salad',
    89: 'shrimp_and_grits',
    90: 'spaghetti_bolognese',
    91: 'spaghetti_carbonara',
    92: 'spring_rolls',
    93: 'steak',
    94: 'strawberry_shortcake',
    95: 'sushi',
    96: 'tacos',
    97: 'takoyaki',
    98: 'tiramisu',
    99: 'tuna_tartare',
    100: 'waffles'
    }
    class_name = class_names[class_index]
    
    # Return the predicted class name as the API response
    return {'class': class_name}

# Run the Flask app
if __name__ == '__main__':
    app.run()



