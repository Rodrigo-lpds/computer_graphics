import numpy as np
from ray import Ray
from sphere import Sphere

class SceneManager:
    def __init__(self):
        self.spheres = [
            Sphere(np.array([0.0, 0.0, 2.0]), 0.5, np.array([1.0, 0.0, 0.0]), 0.5),   # Red sphere
            Sphere(np.array([-1.0, -0.5, 3.0]), 1.0, np.array([0.0, 1.0, 0.0]), 0.2),  # Green sphere
            Sphere(np.array([1.0, 1.0, 4.0]), 1.5, np.array([0.0, 0.0, 1.0]), 0.7),   # Blue sphere
            Sphere(np.array([-2.0, 2.0, 5.0]), 0.8, np.array([1.0, 1.0, 0.0]), 0.3),  # Yellow sphere
            Sphere(np.array([2.0, -1.0, 6.0]), 0.7, np.array([1.0, 0.0, 1.0]), 0.6)   # Magenta sphere
        ]
        self.light_position = np.array([2.0, 2.0, -1.0])
        self.light_intensity = 1.0

    def trace_ray(self, ray, depth=0):
        if depth > 3:
            return np.array([0.5, 0.5, 0.5])  # Background color
        
        closest_t = np.inf
        closest_sphere = None
        
        # Find closest intersection with spheres
        for sphere in self.spheres:
            t = sphere.intersect(ray)
            if t < closest_t:
                closest_t = t
                closest_sphere = sphere
        
        # If no intersection, return background color
        if closest_sphere is None:
            return np.array([0.5, 0.5, 0.5])  # Background color
        
        # Calculate intersection point and normal
        hit_point = ray.origin + closest_t * ray.direction
        normal = (hit_point - closest_sphere.center) / closest_sphere.radius
        
        # Calculate shading
        view_dir = -ray.direction
        color = closest_sphere.color
        reflection_coefficient = closest_sphere.reflection_coefficient
        lighting = self.compute_lighting(hit_point, normal, view_dir, color, reflection_coefficient)
        
        # Calculate reflection ray
        reflection_dir = ray.direction - 2 * np.dot(ray.direction, normal) * normal
        reflection_ray = Ray(hit_point, reflection_dir)
        reflection_color = self.trace_ray(reflection_ray, depth + 1)
        
        # Combine shading and reflection
        final_color = lighting + reflection_color * reflection_coefficient
        return np.clip(final_color, 0.0, 1.0)  # Clip values to ensure they are within valid range

    def compute_lighting(self, hit_point, normal, view_dir, color, reflection_coefficient):
        light_dir = self.light_position - hit_point
        light_distance = np.linalg.norm(light_dir)
        light_dir = light_dir / light_distance  # Normalize light direction
        
        # Lambertian shading (diffuse)
        diffuse_intensity = self.light_intensity * max(0.0, np.dot(normal, light_dir))
        
        # Specular reflection (Phong model)
        specular_coefficient = 50.0
        reflect_dir = 2.0 * np.dot(light_dir, normal) * normal - light_dir
        specular_intensity = self.light_intensity * pow(max(0.0, np.dot(reflect_dir, view_dir)), specular_coefficient)
        
        # Combined color
        final_color = color * (diffuse_intensity + specular_intensity * reflection_coefficient)
        return final_color
