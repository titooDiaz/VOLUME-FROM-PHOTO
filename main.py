import sys
import os
import matplotlib.pyplot as plt
from test.create_points import create_points
from test.dot_plot import dot_plot

image_path = "pictures/photo.jpg"
points = 1000
model = "depth-anything/Depth-Anything-V2-Small-hf"

points = create_points(image_path, points, model)

dot_plot(points[0], points[1], points[2])