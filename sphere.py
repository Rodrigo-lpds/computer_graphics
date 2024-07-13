import numpy as np

class Sphere:
    def __init__(self, center, radius, color, reflection_coefficient):
        self.center = center
        self.radius = radius
        self.color = color
        self.reflection_coefficient = reflection_coefficient

    def intersect(self, ray):
        oc = ray.origin - self.center
        a = np.dot(ray.direction, ray.direction)
        b = 2.0 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c
        
        if discriminant < 0:
            return np.inf
        
        t1 = (-b - np.sqrt(discriminant)) / (2.0 * a)
        t2 = (-b + np.sqrt(discriminant)) / (2.0 * a)
        
        if t1 > 0:
            return t1
        elif t2 > 0:
            return t2
        else:
            return np.inf
