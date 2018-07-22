# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:42:49 2018

@author: Logan
"""
import keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classifier=Sequential()

classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation='relu'))

#2max pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())




classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=1,activation='sigmoid'))


classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])



from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen=ImageDataGenerator(rescale=1./255)








 
#training set having the images of various cats and dogs 
training_set=train_datagen.flow_from_directory('dataset/training_set',
                                               target_size=(64,64),
                                               batch_size=32,
                                               class_mode='binary')


#test set having test images for various cats and dogs
test_set=train_datagen.flow_from_directory('dataset/test_set',
                                               target_size=(64,64),
                                               batch_size=32,
                                               class_mode='binary')

classifier.fit_generator(training_set,samples_per_epoch=8000,
                         nb_epoch=2,validation_data=test_set,
                         nb_val_samples=2000)
