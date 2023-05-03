# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import os
from shutil import rmtree

import imageio


def png_to_gif(workdir=r"figures/", png_subdir=r"png/", gif_subdir=r"gif/", **kwargs):
    png_dir = workdir + png_subdir
    gif_dir = workdir + gif_subdir
    images = []

    if os.path.isdir(gif_dir):
        rmtree(gif_dir)
    os.mkdir(gif_dir)

    for file_name in sorted(os.listdir(png_dir)):
        if file_name.endswith(".png"):
            file_path = os.path.join(png_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimwrite(
        gif_dir + r"movie.gif", images, subrectangles=True, **kwargs
    )
