# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:42:48 2018

@author: dutzi
"""

import os
import imageio

png_dir = './png/'
images = []
for file_name in os.listdir(png_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('gif/movie.gif', images)