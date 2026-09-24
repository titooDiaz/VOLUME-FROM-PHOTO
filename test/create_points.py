import torch
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from transformers import AutoImageProcessor, AutoModelForDepthEstimation

def create_points(image_path, NUM_POINTS=1000, MODEL_NAME="depth-anything/Depth-Anything-V2-Small-hf"):
    # CONFIGURATION
    IMAGE_PATH = image_path
    
    # Model
    MODEL_NAME = "depth-anything/Depth-Anything-V2-Small-hf"

    # LOAD MODEL
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
    model = AutoModelForDepthEstimation.from_pretrained(MODEL_NAME)
    model.to(device)
    model.eval()

    # LOAD IMAGE
    image = Image.open(IMAGE_PATH).convert("RGB")
    width, height = image.size


    # DEPTH ESTIMATION
    inputs = processor(images=image, return_tensors="pt")
    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():
        outputs = model(**inputs)
        predicted_depth = outputs.predicted_depth


    # RESIZE DEPTH TO ORIGINAL IMAGE SIZE
    depth = torch.nn.functional.interpolate(
        predicted_depth.unsqueeze(1),
        size=(height, width),
        mode="bicubic",
        align_corners=False
    ).squeeze()

    depth = depth.cpu().numpy()

    # NORMALIZE DEPTH
    depth_min = depth.min()
    depth_max = depth.max()

    depth_normalized = (depth - depth_min)/(depth_max - depth_min)
    # BLUE  = close
    # RED   = far
    depth_for_display = 1.0 - depth_normalized


    # SELECT POINTS

    # Create a regular grid containing approximately
    # NUM_POINTS points.
    grid_size = int(np.sqrt(NUM_POINTS))
    xs = np.linspace(0, width - 1, grid_size)

    ys = np.linspace(0, height - 1, grid_size)
    points = []

    for y in ys:
        for x in xs:
            x_int = int(round(x))
            y_int = int(round(y))
            z = depth_for_display[y_int,x_int]
            points.append((x_int,y_int,z))


    # DISPLAY
    plt.figure(figsize=(12, 8))
    plt.imshow(image)

    # Draw depth-colored points
    scatter = plt.scatter(
        [p[0] for p in points],
        [p[1] for p in points],
        c=[p[2] for p in points],
        cmap="turbo",
        s=40,
        edgecolors="black",
        linewidths=0.5
    )


    plt.colorbar(scatter,label="Relative depth")
    plt.title(f"Depth map - {len(points)} points")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    x_points = []
    y_points = []
    z_points = []
    for x, y, z in points:
        x_points.append(x)
        y_points.append(y)
        z_points.append(z)
    
    return [x_points, y_points, z_points]