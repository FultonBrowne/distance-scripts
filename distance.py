from PIL import Image
import numpy as np
import math

def load_tiff(file_path):
    """
    Load a TIFF depth map and convert it to a NumPy array.
    :param file_path: Path to the TIFF file.
    :return: NumPy array of depth data.
    """
    with Image.open(file_path) as img:
        # Convert image to NumPy array
        depth_map = np.array(img)
    return depth_map

def calculate_distance(depth_map, point1, point2):
    """
    Calculate the Euclidean distance between two points on a depth map.
    :param depth_map: 2D NumPy array of depth values.
    :param point1: Tuple (x1, y1) for the first point.
    :param point2: Tuple (x2, y2) for the second point.
    :return: Distance between the points.
    """
    x1, y1 = point1
    x2, y2 = point2

    # Get depth values for the points
    z1 = depth_map[y1, x1]
    z2 = depth_map[y2, x2]

    print(f"Depth at {point1}: {z1}")
    print(f"Depth at {point2}: {z2}")

    distance = math.sqrt((z1 ** 2) + (z2 ** 2))
    return distance

def main():
    # Path to the TIFF file
    file_path = "image.tiff"

    # Load the depth map
    depth_map = load_tiff(file_path)

    # Define two points (x, y) coordinates
    point1 = (50, 50)
    point2 = (100, 100)

    # Calculate the distance
    distance = calculate_distance(depth_map, point1, point2)

    print(f"Distance between {point1} and {point2}: {distance:.2f} units")

if __name__ == "__main__":
    main()
