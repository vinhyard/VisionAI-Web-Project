
import os

import numpy as np
import pandas as pd

import tensorflow as tf

from matplotlib import pyplot


from sklearn.model_selection import train_test_split

"""

Dataset developed by "Challenges in Representation Learning: A report on three machine learning contests." I Goodfellow, D Erhan, PL Carrier,
A Courville, M Mirza, B Hammer, W Cukierski, Y Tang, DH Lee, Y Zhou, C Ramaiah, F Feng, R Li, X Wang, D Athanasakis, J Shawe-Taylor, M Milakov, J Park, 
R Ionescu, M Popescu, C Grozea, J Bergstra, J Xie, L Romaszko, B Xu, Z Chuang, and Y. Bengrio. arXiv 2013.

"""
"""
#import dataset
df = pd.read_csv("fer2013/fer2013.csv")

"""
#assign numbers to emotions
label_to_text = {0:"anger", 1:"disgust", 2:"fear", 3:"happy", 4:"sad", 5:"surprised", 6:"neutral"}


#reshape data
"""""
image_arr = df.pixels.apply(lambda x: np.array(x.split(' ')).reshape(48, 48).astype('float32'))
image_arr = np.stack(image_arr, axis=0)
labels = df.emotion.values




#train models
X_train, X_test, y_train, y_test = train_test_split(image_arr, labels, test_size = .1)

#divide images to go from 0-255 range to 0-1
X_train = X_train/255
X_test = X_test/255


#model
basemodel = tf.keras.models.Sequential([tf.keras.layers.Conv2D(32, (3, 3), activation = "relu", input_shape = (48, 48, 1)),
                                        tf.keras.layers.MaxPool2D(2, 2),
                                        tf.keras.layers.BatchNormalization(), #normalize data after every iteration
                                        
                                        tf.keras.layers.Conv2D(64, (3, 3), activation = "relu", input_shape = (48, 48, 1)),
                                        tf.keras.layers.MaxPool2D(2, 2),
                                    
                                        tf.keras.layers.Conv2D(128, (3, 3), activation = "relu", input_shape = (48, 48, 1)),
                                        tf.keras.layers.MaxPool2D(2, 2),
                                                                            
                                        #extra layer added to help solve validation accuracy
                                        tf.keras.layers.Conv2D(256, (3, 3), activation = "relu", input_shape = (48, 48, 1)),
                                        tf.keras.layers.MaxPool2D(2, 2),
                                        #flatten output after coming out from maxpool
                                        tf.keras.layers.Flatten(),

                                        #dense layer
                                        tf.keras.layers.Dense(1000, activation='relu'),

                                        #dense layer with soft max because of multi-class
                                        #7 defines the final number of classes. 
                                        tf.keras.layers.Dense(7, activation='softmax')
                                        ])

basemodel.compile(optimizer = tf.keras.optimizers.RMSprop(learning_rate=.0001),
        loss='sparse_categorical_crossentropy', #helps prevent potential bug
        metrics=['accuracy'])


#create a checkpoint folder
try:

    os.mkdir('checkpoint')

except:

    pass

"""
file_name = 'faceexp_model.h5'

checkpoint_path = os.path.join("checkpoint", file_name)

#Validation accuracy
call_back = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                            monitor="val_accuracy",
                                            verbose=1,
                                            save_freq = 'epoch',
                                            save_best_only = True,
                                            save_weights_only = False,
                                            mode='max')

#fit the basemodel
#validation split from .1 -> .2 because small list of images were not accuracte
#basemodel.fit(X_train, y_train, epochs=20, validation_split=.2, callbacks=call_back)


"""
predict_mood example request:
    print(predict_mood('example.jpg'))

    example return: Happy
"""


def predict_mood(photo):
    try:


        final_model = tf.keras.models.load_model('checkpoint/faceexp_model.h5')
        photo_reshape = photo.reshape((48, 48))
        predict_emotion = final_model.predict(tf.expand_dims(photo, 0)).argmax()

        print(f"Mood: {label_to_text[predict_emotion]}")
        return label_to_text[predict_emotion]


    except:

        return "Models not trained"


print(predict_mood("static/Images/kobe.jpg"))