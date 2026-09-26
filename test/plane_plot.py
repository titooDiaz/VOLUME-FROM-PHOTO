import matplotlib.pyplot as plt
import numpy as np

def next_3_points(points_num, points):
    grid = int(np.sqrt(points_num))
    
    for u in range(0, grid-1):
        for i in range(0, grid-1):
            
            # pointed triangle
            print(f"{i+(u*(grid))},{(i+1)+(u*(grid))},{(i+grid)+(u*(grid))}")
            # base triangle
            print(f"{(i+1)+(u*(grid))},{(i+grid)+(u*(grid))},{(i+grid+1)+(u*(grid))}")

next_3_points(9, [1])