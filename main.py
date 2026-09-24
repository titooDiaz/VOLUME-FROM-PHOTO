import sys
import os
from test.create_points import create_points

image_path = "pictures/photo.jpg"
points = 1000
model = "depth-anything/Depth-Anything-V2-Small-hf"

points = create_points(image_path, points, model)