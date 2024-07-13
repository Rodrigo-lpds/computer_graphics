import numpy as np
import matplotlib.pyplot as plt
from ray import Ray
from sphere import Sphere
from scene_manager import SceneManager

# Constants
WIDTH = 1000
HEIGHT = 800

# Main rendering loop
def render_scene():
    scene_manager = SceneManager()
    image = np.zeros((HEIGHT, WIDTH, 3))
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Calculate ray direction through pixel (x, y)
            aspect_ratio = WIDTH / HEIGHT
            screen_x = (2 * (x + 0.5) / WIDTH - 1) * aspect_ratio
            screen_y = (1 - 2 * (y + 0.5) / HEIGHT)
            ray_direction = np.array([screen_x, screen_y, 1.0])
            
            # Create ray from camera (positioned at [0, 0, -1])
            ray = Ray(np.array([0.0, 0.0, -1.0]), ray_direction)
            
            # Trace ray and get color
            pixel_color = scene_manager.trace_ray(ray)
            
            # Set pixel color in image
            image[y, x] = pixel_color
    
    return image

# Display and save rendered image
def display_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.savefig('ray_traced_image.png', dpi=300)
    plt.show()

# Render and display the scene
if __name__ == "__main__":
    rendered_image = render_scene()
    display_image(rendered_image)
