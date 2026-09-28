import matplotlib.pyplot as plt
import numpy as np
from .linear_regression import multiple_linear_regression
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def next_3_points(points_num, points):
    grid = int(np.sqrt(points_num))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    verts = []
    
    for u in range(0, grid-1):
        for i in range(0, grid-1):
            # pointed triangle
            # points in x
            x1, x2, x3 = points[0][i+(u*(grid))], points[0][(i+1)+(u*(grid))], points[0][(i+grid)+(u*(grid))]
            # points in y
            y1, y2, y3 = points[1][i+(u*(grid))], points[1][(i+1)+(u*(grid))], points[1][(i+grid)+(u*(grid))]
            # points in z
            z1, z2, z3 = points[2][i+(u*(grid))], points[2][(i+1)+(u*(grid))], points[2][(i+grid)+(u*(grid))]
            
            x = [x1,x2,x3]
            y = [y1,y2,y3]
            z = [z1,z2,z3]
            
            a = multiple_linear_regression(np.array(x),np.array(y),np.array(z))
            a = np.asarray(a, dtype=float).ravel()

            # new triangle
            zp = [a[0] + a[1]*xi + a[2]*yi for xi, yi in zip(x, y)]
            verts.append(list(zip(x, y, zp)))
            
            # base triangle
            # points in x
            x1, x2, x3 = points[0][(i+1)+(u*(grid))], points[0][(i+grid)+(u*(grid))], points[0][(i+grid+1)+(u*(grid))]
            # points in y
            y1, y2, y3 = points[1][(i+1)+(u*(grid))], points[1][(i+grid)+(u*(grid))], points[1][(i+grid+1)+(u*(grid))]
            # points in z
            z1, z2, z3 = points[2][(i+1)+(u*(grid))], points[2][(i+grid)+(u*(grid))], points[2][(i+grid+1)+(u*(grid))]
            
            x = [x1,x2,x3]
            y = [y1,y2,y3]
            z = [z1,z2,z3]
                        
            a = multiple_linear_regression(np.array(x),np.array(y),np.array(z))
            a = np.asarray(a, dtype=float).ravel()
            
            # new triangle
            zp = [a[0] + a[1]*xi + a[2]*yi for xi, yi in zip(x, y)]
            verts.append(list(zip(x, y, zp)))

    tri = Poly3DCollection(verts, facecolor="tab:blue", edgecolor="k", linewidths=0.2)
    ax.add_collection3d(tri)
    
    ax.scatter(points[0], points[1], points[2], color="red", s=20)
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
    plt.show()