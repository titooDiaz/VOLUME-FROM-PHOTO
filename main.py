import sys
import os
import matplotlib.pyplot as plt
from test.create_points import create_points
from test.dot_plot import dot_plot
from test.plane_plot import next_3_points

image_path = "pictures/photo.jpg"
points_num = 500
model = "depth-anything/Depth-Anything-V2-Small-hf"

points = create_points(image_path, points_num, model)

dot_plot(points[0], points[1], points[2])

next_3_points(points_num, points)