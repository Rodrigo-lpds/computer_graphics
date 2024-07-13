# Ray Tracing in Python

This project implements a ray tracing algorithm in Python for the final computer graphics homework at UFRJ, under the supervision of Professor Ricardo Farias. The implementation demonstrates fundamental concepts of computer graphics, including ray-sphere intersection, lighting models, and recursive reflection.

## Features

- **Ray Class**: Represents rays with an origin and direction vector.
- **Sphere Class**: Defines spheres with properties such as center, radius, color, and reflection coefficient.
- **SceneManager**: Manages the scene setup including spheres, light position, and intensity.
- **Lambertian Shading**: Implements diffuse reflection using Lambertian shading.
- **Phong Model**: Computes specular highlights for reflective surfaces.
- **Recursive Ray Tracing**: Calculates reflections recursively to simulate reflective surfaces.
- **Rendering Loop**: Generates an image from the scene setup using ray tracing.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rodrigo-lpds/computer_graphics.git
   cd computer_graphics
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to render the scene and display the image:

```bash
python main.py
```

The rendered image will be saved as `ray_traced_image.png` in the project directory.

## Scene Configuration

Modify `scene_manager.py` to adjust the spheres, their positions, colors, and reflection coefficients. You can also change the light source's position and intensity to experiment with different scenes.

## Acknowledgments

- Developed as the final computer graphics homework for Professor Ricardo Farias' course at UFRJ.
- Inspired by principles of ray tracing and computer graphics.

---