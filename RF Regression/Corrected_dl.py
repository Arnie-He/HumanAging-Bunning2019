from __future__ import absolute_import
from matplotlib import pyplot as plt

import os
import tensorflow as tf
import numpy as np
import random
import math

class Model(tf.keras.Model):
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
    
    def call(self, inputs, is_testing = False):

    def loss(self, logits, labels):

    def accuracy(self, logits, labels):


def train(model, train_inputs, train_labels):
    